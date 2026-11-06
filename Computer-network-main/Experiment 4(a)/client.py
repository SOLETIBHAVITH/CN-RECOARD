import socket

try:
    with socket.create_connection(("127.0.0.1", 31001), timeout=30) as connection:
        print("Connected to echo server")
        message = input("Enter message: ")
        connection.sendall((message + "\n").encode("utf-8"))
        with connection.makefile("r", encoding="utf-8") as reader:
            reply = reader.readline()
            if reply:
                print("Server replied:", reply.rstrip("\n"))
            else:
                print("Server closed without a reply")
except (OSError, EOFError, UnicodeError) as error:
    print("Echo client error:", error)
