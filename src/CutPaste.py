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

def cut(fileName, v=0):
    #checks if argument is used
    if fileName[0] in ["-f", "-F"]:
        v = int(fileName[1]) - 1
        del fileName[0:2]
    # opens file
    for i in fileName:
        with open(i, "r") as fle:
            lines = fle.readlines()
            header = lines[v].split(",")
            tbd = [header[v]]
            for j in lines[0:]:
                row = j.split(",")
                for k in range(len(tbd)):
                   print(row[v])



def paste(files):
    contents = []
    for i in files:
        with open(i, "r") as f:
            contents.append(f.readlines())

    maxLen = max(len(l) for l in contents)

    for i in range(maxLen):
        lines = []
        for j in contents:
            if i > len(j):
                line = ""
            else:
                line = j[i].strip("\n")
            lines.append(line)
        for n in range(len(lines)):
            print(lines[n]+",", end="")
        print("")