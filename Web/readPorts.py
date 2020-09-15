import serial.tools.list_ports 
#import alertMsg as al
global ports
def readPort():
    ports = list(serial.tools.list_ports.comports())
    print(ports)
    if len(ports) == 0:
        print("a")
        al.altPort()
        p=[1,2]
    else:
        for p in ports:
            print (p[0])        
    return p[0]

def readPortW():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
        pw = str(p)
        if pw[7] == 'A':
            print("encontrado: ",pw)
            return pw
#readPortW()