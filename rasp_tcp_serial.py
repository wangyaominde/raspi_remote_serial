import serial_local
import udp_raspberry_client

udp_addr, udp_port = udp_raspberry_client.get_trans_port_address()

print("UDP: %s:%d" % (udp_addr, udp_port))
ser_list=serial_local.get_all_serial_port()
print(ser_list)
udp_raspberry_client.send_data(udp_ser_address=udp_addr,udp_ser_port=udp_port,data=ser_list)