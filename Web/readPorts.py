import serial.tools.list_ports 
def readPort():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print (p[0]) 
    return p[0]
#readPort()