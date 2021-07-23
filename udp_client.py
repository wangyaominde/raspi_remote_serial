import socket

def udp_client(host,port):
    """creare udp client use port"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto("hello",(host,port))
    data, addr = sock.recvfrom(1024)
    print ("received:", data, "from", addr)

udp_client("192.168.9.201",8888)