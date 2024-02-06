#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.

from Usage import usage
def cat(fileName):
    if len(fileName) == 0:
        usage(error="too few arguments", tool="cat")
    # this is to iterate through all files
    for i in fileName:
        # this opens one file at a time
        with open(i, 'r') as file:
            # this prints the entire file
                print(file.read(), end="")


def tac(fileName):
    if len(fileName) == 0:
        usage(error="too few arguments", tool="tac")
    #iterate trough each file
    for i in fileName:
        with open(i, "r") as f:
            #seperate each line
            line = f.readlines()
            #reverse lines
            line.reverse()
            #print contents line by line
            for j in line:
                print(j, end="")
