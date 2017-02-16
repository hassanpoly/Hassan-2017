#!/usr/bin/python
##djtgcfg prog -d JtagSmt1 -i 0 -f adder_dut.bit 




import serial, time
from addresstable import *
import binascii
ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 38400
ser.bytesize = serial.EIGHTBITS 
ser.parity = serial.PARITY_NONE 
ser.stopbits = serial.STOPBITS_ONE              
ser.xonxoff = False    
ser.rtscts = False    
ser.dsrdtr = False  
number_address = 10
number_char = 9  
timeout=1
#f=open('lut.txt','r')
  
try: 
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():

    try:
         ser.flushInput()
	 ser.flushOutput()
# reading        
         max_packet = 20
         lines = 0
         while True:
           byteData = ser.read_until('\r',max_packet)
	   newdata=str(byteData)
           print newdata.strip()
                
	   ser.write('I')
           time.sleep(0.01)
# writing
           with open('lut.txt', 'r') as f:
            for line in f.readlines():
             #print line
             ser.write('N')
             time.sleep(0.01)
             ser.write(' ')
             time.sleep(0.01)
             ser.write('C')
             time.sleep(0.01)
             for i in line:
              newdata=i
              ser.write(newdata)
              time.sleep(0.01)
              #ser.write(line[0+i])
             #for line1 in line:
             #line="line"+"0"
             #print len(line)
             #requ = binascii.unhexlify(line)
             #for i in requ:
              #ser.write('line1')
              #time.sleep(0.01)
            #line+=1
            time.sleep(1)
         
 
        
    except Exception, e1:
        print "error communicating...: " + str(e1)

else:
    print "cannot open serial port "
