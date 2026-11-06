# Experiment 3 - HTTP Web Client Using TCP Sockets

Aim:

To request and receive a webpage through a TCP socket using plaintext HTTP.

Algorithm:

1. Read the server host, port and request path.
2. Create a TCP connection and send a complete HTTP GET request.
3. Read the response headers and body with the standard HTTP response parser.
4. Display the status, body size and webpage content.
5. Close the response and socket; report connection or HTTP errors.

Program / Commands:

[Source: client.py](client.py)

```powershell
python client.py
# Public HTTP example, with explicit arguments:
python client.py example.com 80 /
```
The parser handles Content-Length, chunked bodies and connection-close framing. This is an HTTP client; HTTPS requires TLS and is not implemented. It does not follow redirects or interpret HTML.

Output / Observation:

Execution Status: Verified

Public endpoint example.com:80 returned this actual HTTP response. Separate localhost tests also verified multi-read Content-Length and chunked response bodies.

```text
HTTP status: 200 OK
Body bytes: 577
<!doctype html><html lang=en><head><meta charset=utf-8><link rel=icon href=data:,><meta name=viewport content="width=device-width,initial-scale=1"><title>Example Domain</title><style>html{color-scheme:light dark;background:light-dark(#eee,#222)}body{font:16px/1.6 system-ui,sans-serif;max-width:26em;margin:auto;padding:25vh 2em 2em;text-align:center}</style></head><body><p>This domain is for use in documentation examples without needing permission. This is not a service; avoid relying on it for testing and monitoring purposes.</p><script src=/s.js></script></body></html>
```
