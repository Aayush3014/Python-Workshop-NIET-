l = []
count = 0
ans = "y"
while ans=="y":
    num = int(input("enter the number : "))
    l.append(num)
    if num>0:
        count+=1
        ans = input("Want to enter more number? (y/n) : ")
else:
    print(f"You entered  {count} numbers ")
    print("Largest number from all you entered is : ",max(l))