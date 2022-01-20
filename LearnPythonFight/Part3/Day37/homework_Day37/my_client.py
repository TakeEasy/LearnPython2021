import socket
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    msg = input('请输入命令:').strip()
    if len(msg) == 0: continue
    client.send(msg.encode('utf-8'))
    header = client.recv(4)
    total_size = struct.unpack('i', header)[0]
    recv_size = 0
    cmd_res = b''

    while recv_size < total_size:
        recv_data = client.recv(1024)
        recv_size += len(recv_data)
        # cmd_res += recv_data
        print(recv_data.decode('utf-8'), end='')
    else:
        print()
