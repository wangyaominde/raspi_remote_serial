# -*- coding: utf-8 -*-
# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060
def set_port_address(port_num):
    network = '<broadcast>'
    port_n = 8888
    s.sendto(('raspi_remote_serial use port = '+str(port_n)).encode('utf-8'), (network, PORT))
    s.close()