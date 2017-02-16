#!/usr/bin/python
import serial
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
print "connected to: " + ser.portstr
count=0
while True:
     for line in ser.readlines():   
          print  line
          count=count+1

ser.close()   
