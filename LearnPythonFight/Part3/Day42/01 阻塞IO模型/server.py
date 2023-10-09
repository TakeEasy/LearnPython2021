import socket


server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)


while True:
    conn, addr = server.accept()
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:break
            print(data)
            conn.send(data.upper())
        except ConnectionResetError as e:
            break
    conn.close()