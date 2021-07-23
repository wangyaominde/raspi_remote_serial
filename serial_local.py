import serial

def get_all_serial_port():
    """
    获取当前系统所有可用串口
    :return:
    """
    port_list = []
    port_list = serial.tools.list_ports.comports()
    return port_list

print(get_all_serial_port())