import serial_local
import udp_raspberry_client
import json

udp_addr, udp_port = udp_raspberry_client.get_trans_port_address()

print("UDP: %s:%d" % (udp_addr, udp_port))
<<<<<<< HEAD

=======
>>>>>>> 3fcca0465abed96ed3dc0021b32a363d420e66fe
def send_serial_list():
    ser_list=serial_local.get_all_serial_port()
    udp_raspberry_client.send_data(udp_ser_address=udp_addr,udp_ser_port=udp_port,data=json.dumps(ser_list))

<<<<<<< HEAD
send_serial_list()
=======
>>>>>>> 3fcca0465abed96ed3dc0021b32a363d420e66fe
