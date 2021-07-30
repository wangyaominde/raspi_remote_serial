import serial_local
import udp_raspberry_client
import json

udp_addr, udp_port = udp_raspberry_client.get_trans_port_address()

print("UDP: %s:%d" % (udp_addr, udp_port))
def send_serial_list():
    ser_list=serial_local.get_all_serial_port()
    print(ser_list)
    udp_raspberry_client.send_data(udp_ser_address=udp_addr,udp_ser_port=udp_port,data=json.dumps(ser_list))

def get_data_from_serial(ser_port,ser_baud,ser_timeout):
    """get data from serial to udp server"""
    ser_data=serial_local.get_data_from_serial(ser_port=ser_port,ser_baud=ser_baud,ser_timeout=ser_timeout)
    ser_data_json=json.dumps(ser_data)
    udp_raspberry_client.send_data(udp_ser_address=udp_addr,udp_ser_port=udp_port,data=ser_data_json)

def write_data_to_serial(ser_port,ser_baud,ser_timeout,ser_data):
    """write data to serial from udp server"""
    serial_local.write_data_to_serial(ser_port=ser_port,ser_baud=ser_baud,ser_timeout=ser_timeout,ser_data=ser_data)

send_serial_list()