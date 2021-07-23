# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

network = '<broadcast>'
s.sendto('this program for udp get ip'.encode('utf-8'), (network, PORT))