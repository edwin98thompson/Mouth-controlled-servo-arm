import serial

import time


def bluetooth_handler(port, data):
    # try:
    bluetooth = serial.Serial(port, 9600, timeout=0)
    bluetooth.write(data.encode())
    print("sent")
    bluetooth.close()
    # except serial.SerialException:
    # print("Bluetooth connection not configured")


#bluetooth_handler('COM9', '1')

# class Bluetooth_handler:
#     def __init__(self, port):
#         self.port = port
#         #self.bluetooth = serial.Serial(self.port, 9600)
#
#     def connect(self):
#         try:
#             self.bluetooth = serial.Serial(self.port, 9600)
#             print("Bluetooth connected")
#         except serial.SerialException:
#             print("Bluetooth connection not successful.")
#         except serial.SerialTimeoutException:
#             print("Bluetooth connection timed out.")
#
#     def send_data(self):
#         self.bluetooth.write()
#


# def bluetooth_connect(port):
#     try:
#         bluetooth = serial.Serial(port, 9600)
#         # print("Bluetooth connected")
#     except serial.SerialException:
#         print("Bluetooth connection not configured")
