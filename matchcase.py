cmd = "GET /index.html"
match cmd.split():
    case ["GET", path]:
        print(f"GET request for {path}")
    case ["POST", path, data]:
        print(f"POST request for {path} with data: {data}")
    case _:
        print("Unknown command")