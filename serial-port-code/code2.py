#!/usr/bin/ python
import serial

from time import time
from sys import argv
from serial import Serial

#rate = argv[]
#if rate != 0 and rate != 1:
   # rate = 0

#rates = [460800, 115200]

#print("setting rate to: ", rates[rate])

conn = Serial('/dev/ttyUSB0', baudrate=115200, timeout=2)


def read_dimension(dimension):
    global conn
    failure_count = 0
    # the serial connection often fails to read two single bytes
    while True:
        try:
            #conn.write(dimension)
            value =chr(conn.read(1))
            value +=chr(conn.read(1)) << 8
            return value
        except Exception as e:
            failure_count += 1

if __name__ == "__main__":
    while True:
        start = time()
        x_val = read_dimension(b'x')
        #y_val = read_dimension(b'y')
        #z_val = read_dimension(b'z')
        print(x_val)

