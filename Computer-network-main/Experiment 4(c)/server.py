import argparse
from pathlib import Path
import socket
import struct

parser = argparse.ArgumentParser(description="Send one local file over loopback TCP.")
parser.add_argument("file", type=Path)
args = parser.parse_args()

try:
    with args.file.open("rb") as source, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", 31003))
        server.listen(1)
        print("File server ready on localhost:31003", flush=True)
        connection, _ = server.accept()
        with connection:
            connection.settimeout(30)
            size = args.file.stat().st_size
            connection.sendall(struct.pack("!Q", size))
            remaining = size
            while remaining:
                block = source.read(min(4096, remaining))
                if not block:
                    raise OSError("Source file changed during transfer")
                connection.sendall(block)
                remaining -= len(block)
            print("Sent bytes:", size)
            if connection.recv(1) == b"K":
                print("Client confirmed complete transfer")
            else:
                print("Client did not confirm transfer")
except OSError as error:
    print("File server error:", error)
