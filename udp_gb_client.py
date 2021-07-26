# udp_gb_client.py
'''客户端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

s.bind(('', PORT))
print('Listening for broadcast at ', s.getsockname())


def get_tcp_port_address():
    while True:
        data, address = s.recvfrom(65535)
        if data.startswith(b'raspi_remote_serial use port = '):
            print('Server: ', address, data)
            tcp_ser_addr=address
            tcp_ser_port=data[-4:]
        break

    tcp_ser_addr=tcp_ser_addr[0]
    tcp_ser_port=int(tcp_ser_port)
    #print('tcp_ser_addr=',tcp_ser_addr)
    #print('tcp_ser_port=',tcp_ser_port)
    return tcp_ser_addr,tcp_ser_port

