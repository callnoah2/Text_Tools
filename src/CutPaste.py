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

def cut(fileName, n=0):
    #checks if argument is used
    if fileName[0] in ["-f", "-F"]:
        n = int(fileName[1]) - 1
        oracleN = fileName.split(",")
        del fileName[0:2]
    # opens file
    for i in fileName:
        with open(i, "r") as fle:
            #splits by lines
            lines = fle.readlines()
            header = lines[n].split(",")
            # determines what col to print
            col = [header[n]]
            #spits all lines by comma
            for j in lines[0:]:
                row = j.split(",")
                #prints all rows at the correct col
                for k in range(len(col)):
                   print(row[n])





def paste(files):
    #empty string to add all files to
    contents = []
    #opens each file
    for i in files:
        with open(i, "r") as f:
            #splits files into seperate lines and adds them to list
            contents.append(f.readlines())
    #determines what the longest file is
    maxLen = max(len(l) for l in contents)

    #for the length of the longest file:
    for i in range(maxLen):
        lines = []
        #for each line in contents
        for j in contents:
            # checks to see if file is still going, if not, prints empty string
            if i > len(j):
                line = ""
            else:
            #if string is not empty, print the line without "\n"
                line = j[i].strip("\n")
            lines.append(line)
        for n in range(len(lines)):
            print(lines[n]+",", end="")
        #prints newline
        print("")