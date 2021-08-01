# -*- coding: utf-8 -*-

import udp_pc_server
import socket
import json

udp_port=8888

udp_pc_server.set_port_address(port_num=udp_port)

def udp_server_main(port_number):
    """持续获取udp数据,使用port_number"""
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind(('', port_number))
    while True:
        data = udp_server_socket.recvfrom(1024)
        print(json.loads(data.decode()))

udp_server_main(udp_port)
    