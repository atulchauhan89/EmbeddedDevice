from serial.tools.list_ports import comports
import serial


#   Get ALL the port
def get_ports():
    total_ports = comports()
    return total_ports
    # print(all_ports[0])


def find_port():
    comm_port = 'None'
    all_ports = get_ports()
    num_connection = len(all_ports)
    try:
        for i in range(0, num_connection):
            port = all_ports[i]
            str_port = str(port)

            if 'PI USB to Serial' in str_port:
                splitport = str_port.split(' ')
                comm_port = (splitport[0])

        return comm_port
    except:
        print("USB is not connected properly with Updater, "
              "Please connect and retry")

#
# if __name__ == '__main__':
#     connectPort = find_port()
#     if connectPort != 'None':
#         ser = serial.Serial(connectPort, baudrate=9600, timeout=1)
#         print('Connected to ' + connectPort)
#
#     else:
#         print('Connection Issue!')
#
#     print('DONE')
