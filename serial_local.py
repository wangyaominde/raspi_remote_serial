import serial

def get_all_serial_port():
    """
    获取当前系统所有可用串口
    :return:
    """
    port_list = []
    for port in list(serial.tools.list_ports.comports()):
        port_list.append(port[0])
    return port_list

print(get_all_serial_port())