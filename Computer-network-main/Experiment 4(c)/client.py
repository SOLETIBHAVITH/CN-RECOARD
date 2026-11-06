import argparse
from pathlib import Path
import socket
import struct

parser = argparse.ArgumentParser(description="Receive a file without overwriting an existing file.")
parser.add_argument("output", type=Path)
args = parser.parse_args()

try:
    with socket.create_connection(("127.0.0.1", 31003), timeout=30) as connection:
        header = b""
        while len(header) < 8:
            block = connection.recv(8 - len(header))
            if not block:
                raise OSError("Connection closed before file length arrived")
            header += block
        size = struct.unpack("!Q", header)[0]
        with args.output.open("xb") as destination:
            remaining = size
            while remaining:
                block = connection.recv(min(4096, remaining))
                if not block:
                    raise OSError("Connection closed before the complete file arrived")
                destination.write(block)
                remaining -= len(block)
        connection.sendall(b"K")
        print("Received bytes:", size)
        print("Saved:", args.output)
except OSError as error:
    print("File client error:", error)
