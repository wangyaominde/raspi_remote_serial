# -*- coding: utf-8 -*-
import mqtt_client_send
import serial_local
import json

ser_port_list = serial_local.get_all_serial_port()
mqtt_client_send.mqtt_client_send("serial_port_number", json.dumps(ser_port_list))
print(ser_port_list)