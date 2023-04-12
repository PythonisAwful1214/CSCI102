#   Nicolas Callier
#   CSCI102 - Section H
#   Assessment 05A
#   Time 20 minutes

print("Enter values to add.  Enter quit when done.")

imp = 0
l = []
while imp != "quit":
    l.append(int(imp))
    imp = input("NUMBER> ")

tot = 0
for i in l:
    tot += i
print("The addition of the " + str(len(l)-1) + " numbers entered is:\nOUTPUT " + str(len(l)-1) + " numbers \nOUTPUT " + str(tot) + " total")
