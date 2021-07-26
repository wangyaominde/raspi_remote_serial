import socket
import time

def connect_tcp_server(host,port):
    """connect tcp server use port"""
    while True:
        print(host,port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.send("Hello, I am a client".encode("utf-8"))
        print(sock.recv(1024).decode("utf-8"))
        sock.close()
        time.sleep(3)

