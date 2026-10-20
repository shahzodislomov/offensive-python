ports = [21,22,80,443]
ports.append(8080)
print(ports)
del ports[1]
print(ports)
top3 = ports[:3]
print(top3)
print(ports[::-1])