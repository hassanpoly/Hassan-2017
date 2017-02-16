#!/usr/bin/env python
          
      
import serial
import time
ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1)
print "OK OPENED SERIAL:",ser
time.sleep(1)
print "READ:",repr(ser.read(1000))
