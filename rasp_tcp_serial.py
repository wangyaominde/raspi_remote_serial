import serial_local
import udp_gb_client

tcp_addr,tcp_port = udp_gb_client.get_tcp_port_address()
print("tcp_addr:",tcp_addr)
print("tcp_port:",tcp_port)