#   Nicolas Callier
#   CSCI102 Section H
#   Assessment07-checkerboard.py
#   Time it took: 45 minutes

col = int(input("How many columns does the checkerboard have?\n COLUMNS> "))
row = int(input("How many rows does the checkerboard have?\n ROWS> "))
first = input("What are the strings with which to pattern it?\n FIRST> ")
second = input("SECOND> ")

eL = []

for i in range(0,row):
    x = 0
    if i %2 != 0:
        x = 1
    balls = []
    for j in range (0,col):
        if (j + x) %2 == 0:
            balls.append(first)
        else:
            balls.append(second)
    print("OUTPUT " + str(balls))
    eL.append(balls)

print("OUTPUT " + str(eL))
