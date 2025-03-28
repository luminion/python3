"""
套接字socket
"""

def main():
    import socket
    s = socket.socket()
    addr =('127.0.0.1', 8081) # 元组
    s.connect(addr) # 连接服务器
    print("连接服务器成功,请输入消息")
    msg =  input() # 输入消息
    s.send(msg.encode())
    resp = s.recv(1024)
    print(resp.decode())
    s.close()
main()