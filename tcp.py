import socket
import threading


class tcp():
    def tcp_server(self, host,port):
        """create tcp server use port"""
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Waiting for a connection...")
        self.client_socket, self.client_address = self.server_socket.accept()
        print("Client connected: %s:%s" % self.client_address)


    def tcp_client(self, host, port):
        """create tcp client use host and port"""
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print("Connected to server at %s:%s" % (self.host, self.port))

