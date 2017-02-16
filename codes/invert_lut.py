
#!/usr/bin/python
f = open('adder_dut.xdl','r')
filedata = f.read()

#newdata = filedata.replace("#LUT:O6=","#LUT:O6=~")
newdata=filedata.replace("#LUT:O5=","#LUT:O5=~") 
dst1 = open('temp.xdl','w')
dst1.write(newdata)
dst1.close()



f = open('temp.xdl','r')
filedata = f.read()

#newdata = filedata.replace("#LUT:O6=","#LUT:O6=~")
newdata=filedata.replace("#LUT:O6=","#LUT:O6=~") 
dst = open('adder_lut_inverted.xdl','w')
dst.write(newdata)
dst.close()
