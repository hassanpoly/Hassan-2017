#!/usr/bin/python
import serial


ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 115200

print("connected to: " + ser.portstr)

seq = []
count = 1
ser.open()
#while True:
for c in ser.read(size=1):
        print len(c)
        seq.append(chr(c)) #convert from ANSII
        joined_seq = ''.join(str(v) for v in seq) #Make a string from array

        if chr(c) == '\n':
            print("Line " + str(count) + ': ' + joined_seq)
            seq = []
            count += 1
            break


ser.close()
