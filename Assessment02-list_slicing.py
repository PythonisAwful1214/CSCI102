#   Nicolas Callier, Tony Xie, & Tanner Page
#   CSCI 102 - Section H
#   Assessment 02
#   Time: 25 minutes

print("Enter your string:")
my_str = str(input("STRING>"))
print("Enter four numbers to slice the string")
a = int(input("A> "))
b = int(input("B> "))
c = int(input("C> "))
d = int(input("D> "))
my_str = my_str[(a+1):b] + " " + my_str[(c+1):d] 
print("OUTPUT " + my_str)


