#!/usr/bin/python

import serial, time

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS 
ser.parity = serial.PARITY_NONE 
ser.stopbits = serial.STOPBITS_ONE
#ser.timeout = None         
#ser.timeout = 1              
ser.xonxoff = False    
ser.rtscts = False    
ser.dsrdtr = False  
     
#ser.writeTimeout = 2    
try: 
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():

    try:
        ser.flushInput()
	ser.flushOutput()
	#ser.write('\n')
        #sleep(.1)  
       # numOfLines = 0

       # f=open('signature.txt','w+')

        while True:
          #ser.setTimeout(1)
          #result = ser.read(1)
         # print len(result)
          
          print repr(ser.read(8))
          #f=ser.write(response)
          #print response
          ser.write('\r\n')
          #ser.close
         # numOfLines = numOfLines + 1
    except Exception, e1:
        print "error communicating...: " + str(e1)

else:
    print "cannot open serial port "
