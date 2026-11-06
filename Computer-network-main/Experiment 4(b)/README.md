# Experiment 4(b) - Chat Application Using TCP Sockets

Aim:

To demonstrate a two-way, one-client TCP chat application.

Algorithm:

1. Start the server on loopback port 31002.
2. Connect the client and let the client send the first newline-terminated message.
3. Read and display the message at the server, then enter a reply.
4. Read and display the reply at the client and repeat in alternating turns.
5. Stop when either peer sends /quit or closes the connection.
6. Close sockets and stream readers.

Program / Commands:

[Server](server.py) | [Client](client.py)

```powershell
# Terminal 1
python server.py
# Terminal 2
python client.py
```
This is a turn-taking chat: client sends, then server replies. Either side can send `/quit` on its turn. Socket reads time out after 120 seconds; console input waits for the user.

Output / Observation:

Execution Status: Verified

The captured output below uses piped input. Input is not echoed, so some prompts share lines.

Client inputs: Hello server, Goodbye. Server replies: Hello client, /quit. Both directions and server-requested exit were verified.

```text
Server:
Chat server ready on localhost:31002
Client: Hello server
Server: Client: Goodbye
Server: Chat closed

Client:
Connected. Send a message first; type /quit to exit.
Client: Server: Hello client
Client: Server: /quit
Chat closed
```
