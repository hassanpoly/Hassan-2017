
#!/usr/bin/env python



#from __future__ import division

import os

from comparaison import *

print("get the function from comparison.py")

folder = "ebcfiles-adder/"

#nom_fichier1 = "sans_adc"
#nom_fichier2 = "avec_adc"

#nom_fichier2 = "Compteur_Test_Inj_Faute"

#nom_fichier1 = "A7_default"
#nom_fichier2 = "Top_Sinus_Position2"

file1 = "adder_dut"
file2 = "adder_lut_inverted"

out1 = file1 + "_vs_" + file2
out2 = file1 + "_vs_" + file2 + "LUT_address"

input_file_extension = ".ebc"
#extension_entree = ".rbt"
output_file_extension = ".txt"

file1 = folder + file1 + input_file_extension
file2 = folder + file2 + input_file_extension
out1 = folder + out1 + output_file_extension
out2 = folder + out2 + output_file_extension


# Open file 1
source1 = open(file1, "r")
 
# Open file 2
source2 = open(file2, "r")


dst1 = open(out1, "w")


dst2 = open(out2, "w")
 
try:
    # Appeler la fonction de traitement
    comparer(source1, source2, dst1, dst2, file1, file2)
finally:
    
    
    dst2.close()

    dst1.close()

    
    source2.close()
    
    source1.close()

    
#os.system("pause")
