
#/usr/bin/env python



import os 

#nb_lignes = 1010909 #Zynq
#nb_bits = 32349088 #Zynq



num_lines=1909514 # for Artix-7
num_bits=61104448 # for Artix-7
bits_perline=32


del_lines=8    # number of header lines; must be deleted



def comparer(src1, src2, dst1, dst2, file1, file2):
    
    
	#output header

    header = "comparison between .ebc file and modified .ebc  " + file1 + " and" + "modified"+ file2+ "\n" \
        + "created by hassan" + "\n" \
        + "\n" \
        + "this code find the difference bwteen two .ebc to locate address of LUTs" + "\n" \
        + "\n" \
        + "Line : " + str(num_lines) + "\n" \
        + "Bits : " + str(num_bits) + "\n" \
        + "\n"

    header2 = "Position of address and bits   of " + file1 + " and " + file2 + "\n" + "\n"
		
    dst1.write(header)
    dst2.write(header2)
    
    i=0
    while i < del_lines:
        line1 = src1.readline()
        line2 = src2.readline()
        
        i+=1
    
   #comparison
    i=0
    correction = ""
    
    if (len(file1) > len(file2)):
        line1_plus_grand = 1
        while i < (len(file1)-len(file2)):
            correction+=" "
            i+=1
        offset = len(file1)
    else:
        line1_plus_grand = 0
        while i < (len(file2)-len(file1)):
            correction+=" "
            i+=1
        offset = len(file2)
           


    num_bit_diff = 0
    num_lines_diff =0

    i=0
    j=0
    k=0
    
    while i < num_lines:
        line1 = src1.readline() 
        line2 = src2.readline() 

        if (line1 != line2):
            num_lines_diff += 1

            a_write1 = "Line " + str(i+1) + " (Line " + str(i+1+del_lines) + " in the file) :\n"
            if line1_plus_grand:
                a_write1 += file1 + " : " + "10987654321098765432109876543210" + "\n"
                a_write1 += file1 + " : " + line1 + file2 + correction + " : " + line2
            else:
                a_write1 += file1 + correction + " : " + "10987654321098765432109876543210" + "\n"
                a_write1 += file1 + correction + " : " + line1 + file2 + " : " + line2
            
            dst1.write(a_write1)
            
            a_write2 = ""
            a_write_file2 = ""
            
            while j < (offset+3): #shift to align with the top line
                a_write2 += " "
                j+=1
            
            while k < bits_perline:
                if ((line1[k] == line2[k])):
                     a_write2 += " "
                else:
                    if (line1[k]==1): 
                        a_write_file2 = str(i+1) + " " + str(31-k) + "\n" + a_write_file2
                        a_write2 += "^"
                        num_bit_diff += 1
                    else:
                        a_write2 += " " 
                            
                k+=1

            dst2.write(a_write_file2)
            a_write2 += "\n" + "\n"
            dst1.write(a_write2)
        
        i+=1
        j=0
        k=0
    
    a_write3 = "Number of different line = " + str(num_lines_diff) + " outof " + str(num_lines) + " percentage of " + str(round(100*num_lines_diff/num_lines, 2)) + "%\n" \
        + "number of different bits = " + str(num_bit_diff) + " outof " + str(num_bits) + " percentage of " + str(round(100*num_bit_diff/num_bits, 2)) + "%\n"
    dst1.write(a_write3)
      
    
    
# test des fonctions
if __name__ == "__main__":
 
    
  print 'Output files generated'
