import socket

def udp_server(port):
    """create udp server use port and localhost"""
    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind socket
    sock.bind(('127.0.0.1', port))
    # listen
    sock.listen(5)
    # accept
    while True:
        data, addr = sock.accept()
        print('Received from {}:{}'.format(addr[0], addr[1]))
        data = data.recv(1024)
        print('Received from {}:{}'.format(addr[0], data.decode()))
        data.send(b'Hello, I am server')
        data.close()

udp_server(8888)