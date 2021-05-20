#Program 6
n = 5
while n>0:
    word = input("Enter the word : ")
    if len(word)>=6:
        print("The word is :",word)
        n-=1
    else:
        print("Enter the word again")

