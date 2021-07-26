import serial

def get_all_serial_port():
    """
    获取当前系统所有可用串口
    :return:
    """
    import serial.tools.list_ports
    return [port[0] for port in serial.tools.list_ports.comports()]


