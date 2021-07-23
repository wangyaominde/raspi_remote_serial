# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

network = '<broadcast>'
tcp_port = 8888
s.sendto(('raspi_remote_serial use port = '+str(tcp_port)).encode('utf-8'), (network, PORT))