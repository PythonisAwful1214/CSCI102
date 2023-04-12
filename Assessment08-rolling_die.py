#   Nicolas Callier
#   CSCI102 SECTION - H
#   Assessment08-rolling_die.py
#   Time it took: 30 minutes

import random
random.seed(int(input("SEED> ")))


rols = (int(input("ROLLS> ")))
sides = (int(input("SIDES> ")))
variablename = []


for i in range (0,sides):
    variablename.append(0)

for i in range(0,rols):
    nu = random.randint(1,sides)
    variablename[nu-1] += 1

for i in range (0,sides):
    print("OUTPUT " + str(i+1) + " occurred " + str(variablename[i]) + " times")