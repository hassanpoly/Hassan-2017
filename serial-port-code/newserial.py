#!/usr/bin/python
##djtgcfg prog -d JtagSmt1 -i 0 -f adder_dut.bit 

import serial, time

ser = serial.Serial()
ser.port = "/dev/ttyUSB2"
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS 
ser.parity = serial.PARITY_NONE 
ser.stopbits = serial.STOPBITS_ONE              
ser.xonxoff = False    
ser.rtscts = False    
ser.dsrdtr = False  
     
  
try: 
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():

    try:
        ser.flushInput()
	ser.flushOutput()
        ser.write('\x0C')
        time.sleep(0.1)

       
        max_packet = 8
        
	while ser.write('\x0C'):
    	   data = ser.read_until(terminator='\r',size=max_packet)
    	   newdata=str(data)
           print newdata.strip()
           if 'please' in newdata.strip():
            ser.Write("\r\n")
           
          
          
         # print repr(ser.read(8))
        
          
    except Exception, e1:
        print "error communicating...: " + str(e1)

else:
    print "cannot open serial port "
