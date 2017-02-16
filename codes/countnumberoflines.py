#!/usr/bin/python
fname="adder_dut.ebd"
num_lines = 0
num_ones=0
ones="1"
with open(fname,'r') as f:

	for line in f:
    		words = line.split()
		num_ones = line.split()
   	        num_lines +=1
		
		

		#bin(num_ones).count("1")
print "Number of lines in the ebd file:"
print (num_lines) 
print "--------------"
file.close(f);
