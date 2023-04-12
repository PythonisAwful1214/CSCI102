#   Nicolas Callier
#   CSCI102 - Section H
#   Time: 30 minutes

import random 
f = open("dictionary.txt", "r")
word = f.read()
x = word.split("\n")

seed = input("Enter the seed to use:\nSEED> ")
length = int(input("Enter the length of the words to find:\nLENGTH> "))
numberofwords = 0

dog = []
for i in x:
    if len(i) == length:
        dog.append(i)
        numberofwords += 1

if len(dog) == 0:
    print(f"There are no words of length {length} in the dictionary.\nOUTPUT None")
    print(f"The number of words with length {length} is:\nOUTPUT 0")

elif len(dog) == 1:
    print(f"Here is the only word with length {length}:\nOUTPUT {dog[0]}")
    print(f"The number of words with length {length} is:\nOUTPUT 1")

else:
    random.seed(seed)
    cat = random.choice(dog)
    print(f"Here is a random word with length {length}:\nOUTPUT {cat}")
    print(f"The number of words with length {length} is:\nOUTPUT {numberofwords}")
