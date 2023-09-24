# Querring user to input text
# Text should have a maximum of 20 characters

while True:
    word=input("Enter a word : ")
    if len(word) <= 20:
        break
    else:
        print("The word you entered exceeds 20 chars")

# counting the number of 'z' characters in the string
numZ=word.count("z")
# counting te number of 'O' characters in the string
numO=word.count("o") 

# checking if the equation '2*numZ=numO' is satsified
if 2*numZ == numO:
    print('Yes')
else:
    print("No")
