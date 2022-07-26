from serial.tools import list_ports

def get_serial_port():
    """
    Returns the serial port of the raspberry pi
    """
    ports = list_ports.comports()
    if len(ports) == 0:
        return None
    else:
        return ports



