import socket

def connect_tcp_server(host,port):
    """connect tcp server use port"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send("Hello, I am a client".encode("utf-8"))
    print(sock.recv(1024).decode("utf-8"))
    sock.close()

connect_tcp_server("192.168.0.195",8888)