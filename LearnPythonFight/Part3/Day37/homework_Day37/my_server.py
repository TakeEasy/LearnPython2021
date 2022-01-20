import socket
import subprocess
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    conn, client_addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
            if len(cmd) == 0: break
            # conn.send(cmd.upper())
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout_res = obj.stdout.read()
            stderr_res = obj.stderr.read()
            total_size = len(stdout_res) + len(stderr_res)
            header = struct.pack('i', total_size)
            conn.send(header)
            conn.send(stdout_res + stderr_res)
        except Exception as e:
            break
