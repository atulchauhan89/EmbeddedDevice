from serial.tools.list_ports import comports
import serial

def get_ports():
    ports = comports()
    return ports
    print(ports[0])

def finddevice(portsFound):
    commPort = 'None'
    numConnection = len(portsFound)

    for i in range(0,numConnection):
        port = foundPorts[i]
        strPort = str(port)

        if 'PI USB to Serial' in strPort:
            splitPort = strPort.split(' ')
            commport   = (splitPort[0])

    return commport


if __name__ == '__main__':
    foundPorts = get_ports()
    connectPort = finddevice(foundPorts)

    if connectPort != 'None':
        ser = serial.Serial(connectPort, baudrate=9600, timeout=1)
        print('Connected to ' +connectPort)
    else:
        print('Connection Issue!')

    print('DONE')
