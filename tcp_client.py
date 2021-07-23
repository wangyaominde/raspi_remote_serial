import socket

def connect_tcp_server(port):
    """connect tcp server use port"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", port))
    sock.send("Hello, I am a client".encode("utf-8"))
    print(sock.recv(1024).decode("utf-8"))
    sock.close()

connect_tcp_server(8888)