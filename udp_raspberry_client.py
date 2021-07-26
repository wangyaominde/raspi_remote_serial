# udp_gb_client.py
'''客户端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

s.bind(('', PORT))

def get_trans_port_address():
    while True:
        data, address = s.recvfrom(65535)
        if data.startswith(b'raspi_remote_serial use port = '):
            print('Server: ', address, data)
            udp_ser_address=address
            udp_ser_port=data[-4:]
        break

    udp_ser_address=udp_ser_address[0]
    udp_ser_port=int(udp_ser_port)
    #print('udp_ser_address=',udp_ser_address)
    #print('udp_ser_port=',udp_ser_port)
    return udp_ser_address,udp_ser_port

def send_data(udp_ser_address,udp_ser_port,data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(data.encode('utf-8'), (udp_ser_address, udp_ser_port))
    s.close()
    