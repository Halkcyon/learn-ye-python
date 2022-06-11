from socket import create_server

RESPONSE = b"HTTP/1.1 200 OK\r\n\r\n"


def make_server():
    s = create_server(("0.0.0.0", 8080))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print("connected from ", addr)

            conn.send(RESPONSE, len(RESPONSE))

            while True:
                data = conn.recv(1024)
                if not data:
                    break

                conn.sendall(data)
