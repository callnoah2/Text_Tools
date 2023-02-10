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
def wc(files):
    if len(files) == 0:
        usage(error="too few arguments", tool="wc")
    # to iterate through each file
    for i in files:
        # to open then close a file as f
        with open(i, "r") as f:
            # count the number of lines
            lines = f.readlines()
            numLines = len(lines)
            # initializing word and character count
            numWords = 0
            numChar = 0
            # loop to iterate though all lines
            for j in lines:
                # counting individual words and characters
                words = j.split()
                numWords += len(words)
                numChar += len(j)

            # print final data

            # Look, I know there was probably a better way to space this,
            #but it took me 30 seconds to write this, another 30 senconds
            #to copy and paste it to work with the other counts.
            #I didn't even know what to look up to find the efficent way to do this
            #so it would have taken much longer.

            #spacing correctly for lines
            if numLines >= 1000:
                lineSpace = " "
            elif numLines >= 100:
                lineSpace = "  "
            elif numLines >= 10:
                lineSpace = "   "
            else:
                lineSpace = "    "

            #spacing correctly for Words
            if numWords >= 1000:
                wordSpace = " "
            elif numWords >= 100:
                wordSpace = "  "
            elif numWords >= 10:
                wordSpace = "   "
            else:
                wordSpace = "    "

            #spacing correctly for Char
            if numChar >= 1000:
                charSpace = " "
            elif numChar >= 100:
                charSpace = "  "
            elif numChar >= 10:
                charSpace = "   "
            else:
                charSpace = "    "
            print(numLines, lineSpace, numWords, wordSpace, numChar, charSpace, i)

