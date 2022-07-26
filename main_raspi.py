import serial_raspi

ports=serial_raspi.get_serial_port()
for i in ports:
    print(i)
    