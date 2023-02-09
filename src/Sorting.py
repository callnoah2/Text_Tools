from Concatenate import cat
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


def sort(fileName):
    # for i in range(len(files)):
    #         with open(files[i], "r") as f:
    #             lines = f.readlines()
    #             lines.sort()
    #             for j in lines:
    #                 finalList.append(j)
    #     sort(finalList)
    #         for k in range(len(finalList)):
    #         print(finalList, end="")

    # finalLst = []
    # for i in range(len(fileName[0])):
    #     with open(fileName[i], "r") as f:
    #         finalLst.append(f.readlines())
    # sort(finalLst)
    # print(finalLst)
    lst = []
    for i in fileName:
        with open(i, "r") as f:
            lst.extend(f.readlines())
    lst.sort()
    for j in lst:
        print(j, end="")

