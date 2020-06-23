import serial
import time
ser = serial.Serial('/dev/ttyACM0',115200)
while 1:
    if (ser.inWaiting()>0):
        myData = ser.readline()
        print(myData)
    
    