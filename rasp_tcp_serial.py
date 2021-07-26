import serial_local
import udp_gb_client

udp_addr, udp_port = udp_gb_client.get_trans_port_address()

print("UDP: %s:%d" % (udp_addr, udp_port))
