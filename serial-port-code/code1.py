#!/usr/bin/ python
import serial
import time
import sys 
import serial
import time
param1 = "/dev/ttyUSB2"
param2 = 115200
#param2=sys.argv[3]
ard = serial.Serial(param1, param2, timeout=0)
RFIDNum = ard.readline() # read all characters in buffer
#time.sleep(1) 
print RFIDNum
