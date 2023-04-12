#   Nicolas Callier, Tanner Page, Tony Xie
#   CSCI102 - Section H
#   Time it took: 3 hours

print("Welcome to our Enhanced Calculator")

operand_one = float(input("Input the first operand\nFIRST> "))

operand_two = float(input("Input the second operand\nSECOND> "))

print("Choose one of the following operations:")
print("1 - addition \n2 - subtraction \n3 - multiplication \n4 - division")

operation = int(input("OPERATION> ")) 

def addZeros(n):
    newS = str(n)[str(n).index("."):]
    while len(newS) != 7:
        newS += "0"
    return str(n)[0:str(n).index(".")] + newS

if operation == 1:
    sum = operand_one + operand_two
    print(f"\nThe result of the addition is:\nOUTPUT {sum:.6f}")
elif operation == 2:
    difference = operand_one - operand_two
    print(f"\nThe result of the addition is:\nOUTPUT {difference:.6f}")
elif operation == 3:
    product = operand_one * operand_two
    print("\nThe result of the multiplication is:\nOUTPUT " + addZeros(product))
elif operation == 4:
    quotient = int(operand_one) // int(operand_two)
    rem = int(operand_one) % int(operand_two)
    print("\nThe result of the division is:\nOUTPUT " + str(quotient) + "\nOUTPUT " + str(rem))
print("Thank you for using our calculator.")