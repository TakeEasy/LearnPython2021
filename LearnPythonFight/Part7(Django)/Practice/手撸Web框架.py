import socket

server = socket.socket()  # TCP
server.bind(('127.0.0.1', 8080))
server.listen(5)
'''
GET / HTTP/1.1\r\n
Host: 127.0.0.1:8080\r\n
Connection: keep-alive\r\n
Cache-Control: max-age=0\r\n
sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"\r\n
sec-ch-ua-mobile: ?0\r\n
sec-ch-ua-platform: "Windows"\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6\r\n
\r\n
'''
while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode('utf-8')
    #忽略请求favicon的请求
    print(data)

    current_path = data.split(' ')[1]
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    if current_path == '/index':
        #conn.send(b'index folder hahaha')
        with open('test_index.html','rb') as f:
            conn.send(f.read())
    elif current_path == '/login':
        conn.send(b'login page heiheihei')
    else:
        conn.send(b'Hellow Web')

    #conn.send(b'HTTP/1.1 200 OK\r\n\r\n Hellow Web')
    conn.close()
