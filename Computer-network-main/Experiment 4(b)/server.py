import socket

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", 31002))
        server.listen(1)
        print("Chat server ready on localhost:31002", flush=True)
        connection, _ = server.accept()
        with connection, connection.makefile("r", encoding="utf-8") as reader:
            connection.settimeout(120)
            while True:
                message = reader.readline()
                if not message:
                    break
                message = message.rstrip("\n")
                print("Client:", message)
                if message == "/quit":
                    break
                reply = input("Server: ")
                connection.sendall((reply + "\n").encode("utf-8"))
                if reply == "/quit":
                    break
        print("Chat closed")
except (OSError, EOFError, UnicodeError) as error:
    print("Chat server error:", error)
