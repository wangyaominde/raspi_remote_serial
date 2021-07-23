import serial

class ser():
    def get_all_serial_port():
        """获取系统所有串口号"""
        import glob
        return glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') + glob.glob('/dev/ttyAMA*')

