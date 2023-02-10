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
def head(files, n=10):
    if len(files) == 0:
        usage(error="too few arguments", tool="head")
    #checks to see if user uses -n argument to change the number of lines
    if files[0] in ["-n", "-N"]:
        if len(files) == 1:
            usage(error="Specify Number of lines.", tool="head")
        n = int(files[1])
        del files[0:2]
    #iterates through all files
    for i in files:
        #opens each file
        with open(i, "r") as f:
            lines = f.readlines()
            #for the first n files, print them
            for j in lines[:n]:
                print(j, end="")


def tail(files, n=10):
    if len(files) == 0:
        usage(error="too few arguments", tool="tail")
    # list to be printed at end
    final =[]
    # checks to see if user uses -n argument to change the number of lines
    if files[0] in ["-n", "-N"]:
        if len(files) == 1:
            usage(error="Specify Number of lines.", tool="tail")
        n = int(files[1])
        del files[0:2]
    # opens each file
    for i in files:
        with open(i, "r") as f:
            lines = f.readlines()
            #reverses so last n lines are on top
            lines.reverse()
            for j in range(n):
                #puts last n lines into the final list
                final.append(lines[j])
            #list reverses back to be printed correctly
            final.reverse()
            #prints each line in the list
            for line in final:
                print(line, end="")
