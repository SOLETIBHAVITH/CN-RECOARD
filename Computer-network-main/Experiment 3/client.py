import argparse
import http.client
import socket

parser = argparse.ArgumentParser(description="Download a page using a plaintext TCP socket.")
parser.add_argument("host", nargs="?", default="example.com")
parser.add_argument("port", nargs="?", type=int, default=80)
parser.add_argument("path", nargs="?", default="/")
args = parser.parse_args()
if not 1 <= args.port <= 65535:
    parser.error("Port must be between 1 and 65535.")
if not args.path.startswith("/") or any(c in args.host + args.path for c in "\r\n"):
    parser.error("Use a hostname and an absolute path without line breaks.")

try:
    with socket.create_connection((args.host, args.port), timeout=10) as connection:
        request = (f"GET {args.path} HTTP/1.0\r\n"
                   f"Host: {args.host}:{args.port}\r\n"
                   "Accept-Encoding: identity\r\nConnection: close\r\n\r\n")
        connection.sendall(request.encode("ascii"))
        # HTTPResponse parses framing; the connection and GET request are made above.
        with http.client.HTTPResponse(connection) as response:
            response.begin()
            body = response.read()
            print("HTTP status:", response.status, response.reason)
            print("Body bytes:", len(body))
            print(body.decode(response.headers.get_content_charset() or "utf-8", errors="replace"))
except (OSError, http.client.HTTPException, UnicodeError, LookupError) as error:
    print("Download failed:", error)
