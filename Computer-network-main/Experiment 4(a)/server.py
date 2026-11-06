import socket

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", 31001))
        server.listen(1)
        print("Echo server ready on localhost:31001", flush=True)
        connection, _ = server.accept()
        with connection, connection.makefile("rb") as reader:
            connection.settimeout(30)
            print("Client connected")
            message = reader.readline()
            if message:
                connection.sendall(message)
                print("Received:", message.decode("utf-8").rstrip("\n"))
                print("Echo sent")
except (OSError, UnicodeError) as error:
    print("Echo server error:", error)
