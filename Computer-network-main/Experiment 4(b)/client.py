import socket

try:
    with socket.create_connection(("127.0.0.1", 31002), timeout=120) as connection:
        print("Connected. Send a message first; type /quit to exit.")
        with connection.makefile("r", encoding="utf-8") as reader:
            while True:
                message = input("Client: ")
                connection.sendall((message + "\n").encode("utf-8"))
                if message == "/quit":
                    break
                reply = reader.readline()
                if not reply:
                    break
                reply = reply.rstrip("\n")
                print("Server:", reply)
                if reply == "/quit":
                    break
        print("Chat closed")
except (OSError, EOFError, UnicodeError) as error:
    print("Chat client error:", error)
