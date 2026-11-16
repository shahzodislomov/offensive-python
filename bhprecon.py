from __future__ import annotations
import asyncio, socket, ssl, json, ipaddress
from pathlib import Path
import httpx, aiodns
from rich.progress import Progress

RESOLVER = aiodns.DNSResolver()
HTTP = httpx.AsyncClient(http2=True, timeout=10.0)


async def resolve(host: str) -> list[str]:
    """Return A/AAAA records for a give host"""
    try:
        ans = await RESOLVER.query(host, "A")
        return [r.host for r in ans]
    except aiodns.error.DNSError:
        return []


async def grab_banner(ip: str, port: int) -> str:
    """naive TCP banner grabber"""
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.write(b"\r\n")
        await writer.drain()
        data = await asyncio.wait_for(reader.read(1024), timeout=4)
        writer.close()
        await writer.wait_closed()
        return data.decode(errors="replace").strip()
    except Exception:
        return ""


async def probe_host(host: str, ports: list[int]) -> dict:
    ips = await resolve(host)
    tasks = [grab_banner(ip, port) for ip in ips for port in ports]
    banners = await asyncio.gather(*tasks)
    return {"host": host, "ips": ips, "banners": banners}


async def main(wordlist: Path, root_domain: str) -> None:
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 465, 587, 993, 995]
    subs = [
        f"{line.strip()}.{root_domain}"
        for line in wordlist.read_text().strip().splitlines()
    ]
    async with Progress() as progress:
        tasks = [probe_host(sub, ports) for sub in subs]
        results = []
        for coro in asyncio.as_completed(tasks):
            result = await coro
            results.append(result)
            progress.update(progress.add_task(result["host"], total=1), advance=1)
    Path("results.json").write_text(json.dumps(results, indent=2))
    print(f"Results saved to results.json")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Banner grabbing and subdomain probing tool"
    )
    parser.add_argument("wordlist", type=Path, help="Path to subdomain wordlist")
    parser.add_argument("root_domain", type=str, help="Root domain to probe")
    args = parser.parse_args()
    asyncio.run(main(args.wordlist, args.root_domain))
