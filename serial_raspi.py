from serial.tools import list_ports

if __name__ == '__main__':
    prots = list_ports.comports()
    for port in prots:
        print(port)
    print('\n')