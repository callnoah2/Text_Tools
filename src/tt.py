#!/usr/bin/env python  	  	  

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


import sys  	  	  

from Concatenate import cat, tac  	  	  
from CutPaste import cut, paste  	  	  
from Grep import grep  	  	  
from Partial import head, tail  	  	  
from Sorting import sort  	  	  
from WordCount import wc  	  	  
from Usage import usage  	  	  


if len(sys.argv) < 2:  	  	  
    usage()  	  	  
    sys.exit(1)  	  	  
else:
    if sys.argv[1] == "cat":
        cat(sys.argv[2:])
    elif sys.argv[1] == "tac":
        tac(sys.argv[2:])
    elif sys.argv[1] == "cut":
        cut(sys.argv[2:])
    elif sys.argv[1] == "paste":
        paste(sys.argv[2:])
    elif sys.argv[1] == "grep":
        grep(sys.argv[2:])
    elif sys.argv[1] == "head":
        head(sys.argv[2:])
    elif sys.argv[1] == "tail":
        tail(sys.argv[2:])
    elif sys.argv[1] == "sort":
        sort(sys.argv[2:])
    elif sys.argv[1] == "wc":
        wc(sys.argv[2:])
    else:
        print("Invalid Tool Selection")
