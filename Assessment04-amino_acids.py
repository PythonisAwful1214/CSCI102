#   Nicolas Callier, 
#   CSCI102 - Section H
#   Assessment 04B
#   References: None
#   Time: 35 minutes

def checker(Test):
    acids = [[3, 7 , 1, 2, 0],[6, 14, 4, 2, 0],[4, 8, 2, 3, 0],[3, 7, 1, 2, 1],[6, 9, 3, 2, 0],[5, 10, 2, 3, 0]]
    for a in range(0, 6):
        num = 0
        for b in range(0, 5):
            if Test[b] == acids[a][b]:
                num += 1
        if num == 5:
          return a

def makeItyouBastard(Test):
    return str(Test[0]) + "C--" + str(Test[1]) + "H--" + str(Test[2]) + "N--" + str(Test[3]) + "O--" + str(Test[4]) + "S"

work = [int(input("CARBON> ")), int(input("HYDROGEN> ")), int(input("NITROGEN> ")), int(input("OXYGEN> ")), int(input("SULFUR> "))]

names = ["Alanine", "Arginine", "Asparagine", "Cysteine", "Histidine", "Glutamine"]
print("OUTPUT " + makeItyouBastard(work))
print("The amino acid entered is:\nOUTPUT " + names[checker(work)])