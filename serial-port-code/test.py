#!/usr/bin python
import time
# code to read the file one by one and remove white space result of the readline process
fo=open('test.txt','r')

for line in fo.readlines():
 recu =  line.strip('\n')
 print recu
 for element in recu:
  print element
  time.sleep(0.5)
