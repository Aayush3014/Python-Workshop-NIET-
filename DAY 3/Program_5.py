n = int(input("Enter the number : "))
try:
    if n>=0:
        print("Entered number is :",n)
except:
    raise Exception("Please enter positive integers.")