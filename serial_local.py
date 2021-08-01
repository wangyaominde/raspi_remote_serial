# -*- coding: utf-8 -*-

import serial

def get_all_serial_port():
    """
    获取当前系统所有可用串口
    :return:
    """
    import serial.tools.list_ports
    return [port[0] for port in serial.tools.list_ports.comports()]


def get_data_from_serial(ser_port, baudrate,timeout):
    """从串口获取数据,返回bytes"""
    ser = serial.Serial(ser_port, baudrate, timeout=timeout)
    data = ser.read_all()
    ser.close()
    return data

def write_data_to_serial(ser_port, baudrate, data):
    """将数据发送到串口"""
    ser = serial.Serial(ser_port, baudrate)
    ser.write(data)
    ser.close()
