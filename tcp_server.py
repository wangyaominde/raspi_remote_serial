import socket

def create_server(port):
    """create a server socket"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(5)
    return server

while 1:
    server = create_server(8888)
    print("Server is listening on port 8888")
    conn, addr = server.accept()
    print("Connection from: {}".format(addr))
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print("Received data: {}".format(data))
        conn.sendall(data)
    conn.close()
