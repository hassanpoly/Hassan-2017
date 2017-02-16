#!/usr/bin/python
filename='ebdfiles/adder_dut.ebd'
countnew=0
with open(filename,'r') as f:
 for line in f:
  print line.strip()
  #number = '1111101101010101010'
  count=line.count('1')
  countnew=countnew+count
  print countnew
