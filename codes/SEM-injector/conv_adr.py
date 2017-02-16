#!/usr/bin/env python

import os 


def converter(src, dst):
    '''
     This code is used to convert the address of the .ebc, .ebd, and rbt files addresses into the SEM injector format
    '''
    src.readline()
    src.readline()


    for line in src :
        elements = line.split()
        
        faulty_line = int(elements[0], 10)-112+10
        faulty_bit = int(elements[1], 10)

        frame = faulty_line // 101
        word = format((faulty_line % 101), '07b')
        bit = format(faulty_bit, '05b')

        concat_word_bit = word + bit

        line = '{0:06x}'.format(frame, 'x').upper() + '{0:03x}'.format(int(concat_word_bit, 2), 'x').upper() + '\n'

        dst.write(line)






	
    # for ligne in src:
        # trame = ligne[0:5] # deja au bon format
        # mot = format(int(ligne[7:9], 16), '07b')
        # bit = format(int(ligne[11:13], 16), '05b')
        
        # concat_mot_bit = mot + bit
		
        # sortie = '0' + trame + format(int(concat_mot_bit, 2), 'x').upper() + '\n'
        ## On ajoute le 0 pour correspondre au code et on met en maj
        
        ## print(trame)
        ## print(mot)
        ## print(bit)
        ## print(concat_mot_bit)
        ## print(sortie)
        
        # dst.write(sortie)

    
# test des fonctions
if __name__ == "__main__":
    
    os.system("pause")
