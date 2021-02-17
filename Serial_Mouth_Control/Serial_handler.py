import serial


def serial_handler(data):
    try:
        arduino_data = serial.Serial('COM7', 9600)
        arduino_data.write(str.encode(data))
        # arduino_resp = arduino_data.readline()
        # print("Arduino response:", arduino_resp.decode('utf-8'))

    except serial.SerialException:
        print("Serial connection not configured")



