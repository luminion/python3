"""
套接字socket
"""
def main():
    import socket
    server =  socket.socket()
    addr =('127.0.0.1', 8081) # 元组
    server.bind(addr) # 绑定地址
    server.listen(5) # 监听
    try:
        while True:
            client, addr = server.accept() # 接收客户端连接
            print("客户端连接成功", client)
            data = client.recv(1024) # 接收客户端发送的数据
            msg = data.decode('utf-8')
            print("客户端发送的数据为:", data.decode('utf-8'))
            resp = "已收到消息"+msg
            client.send(resp.encode()) # 发送数据给客户端
    finally:
        server.close()
main()