import socket

try:
    name = socket.gethostname()
    address = socket.gethostbyname(name)
    print("Host name:", name)
    print("IP address:", address)
except OSError as error:
    print("Host lookup failed:", error)
