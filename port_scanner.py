import socket

target = input("Enter IP address to scan: ")
ports = [21, 22, 23, 80, 443, 8080]

print(f"Scanning {target}...")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()
