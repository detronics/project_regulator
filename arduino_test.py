import time
import serial
import datetime

ser = serial.Serial(port='COM6', baudrate=115200)
received = []

ser.write(b'begin\n')
time.sleep(5)

start = datetime.datetime.now()
for i in range(1, 100):
    ser.write(b'test%i\r\n' % i)
    time.sleep(0.005)
    while ser.inWaiting() > 0:
        line = ser.readline()
        if line:
            received.append(line.decode().strip())

print(datetime.datetime.now() - start)
print(received)