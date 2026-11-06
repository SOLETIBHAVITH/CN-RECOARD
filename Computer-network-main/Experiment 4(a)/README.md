# Experiment 4(a) - Echo Client and Echo Server

Aim:

To send a TCP message to a local server and receive the same message back.

Algorithm:

1. Bind the server to loopback port 31001 and listen.
2. Connect the client and send a UTF-8 line terminated by a newline.
3. Accept the connection and read a complete line, allowing multiple TCP segments.
4. Send that line back and display it at the client.
5. Close both sockets and their file readers.

Program / Commands:

[Server](server.py) | [Client](client.py)

Run in two terminals from this folder:

```powershell
# Terminal 1
python server.py
# Terminal 2
python client.py
```
The server serves one message from one client, then exits. It listens only on 127.0.0.1.

Output / Observation:

Execution Status: Verified

The captured output below uses piped input. Input is not echoed, so some prompts share lines.

Sample input at the client: Hello. Server and client ran on loopback.

```text
Server:
Echo server ready on localhost:31001
Client connected
Received: Hello
Echo sent

Client:
Connected to echo server
Enter message: Server replied: Hello
```
