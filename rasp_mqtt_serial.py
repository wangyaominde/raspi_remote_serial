# -*- coding: utf-8 -*-

import serial_local

ser_port_list = serial_local.get_all_serial_port()
print(ser_port_list)