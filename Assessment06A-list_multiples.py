#   Nicolas Callier
#   CSCI102 Section H
#   Assessment 6
#   TIme: 30 minutes

num = int(input("Enter the number to create multiples for.\n NUMBER> "))
maxindex = int(input("Enter the maximum index of the list.\n INDEX> "))
list = [num]

for i in range(0,maxindex):
    list.append(num * (i+2))

print("Your list of multiples is as follows:\n OUTPUT " + str(list))
print("The first multiple calculated is:\n OUTPUT " + str(num))