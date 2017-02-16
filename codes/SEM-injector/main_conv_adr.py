"""Cette fonction convertit les formats d'adresse d'Injector7 en adresse lineaire pur le SEM
"""

import os

from conv_adr import *

print("Execute function conv_adr.py")

folder = "address-to-convert/"

file1 = "adder-lut-1"

output_file = file1 + "converted"

extension = ".txt"

file1 = folder+file1 + extension
output_file = folder+output_file + extension



source = open(file1, "r")
 

dst = open(output_file, "w")
 
try:
    # Appeler la fonction de traitement
    converter(source, dst)
finally:
    
    # close the output file
    dst.close()
     
    # close the input file
    source.close()

    
os.system("pause")
