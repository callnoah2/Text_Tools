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


def grep(files):
    #see if user is using the -v argument
    if files[0] in ["-v", "-V"]:
        key = files[1]
        del files[0:2]
    #iterate through all files
        for i in range(len(files)):
            #open each file
            with open(files[i], "r") as f:
                lines = f.readlines()
                for j in lines:
                    #if key not in line, print line
                    if key not in j:
                        print(j, end="")
    else:
        # key is the first "file" they put
        key = files.pop(0)
        #iterate through all files
        for i in range(len(files)):
            #open each file
            with open(files[i], "r") as f:
                lines = f.readlines()
                for j in lines:
                    # if key in line print line
                    if key in j:
                        print(j, end="")