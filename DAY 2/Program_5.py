#WAP to dispaly fibonacci series.
num = int(input("Enter number of terms to be printed : "))
if num<=12:
    s = 0
    a = -1
    b = 1
    print("Fibonacci series : ",end=' ')
    for i in range(1,num+1):
        c = a + b
        s += c
        print(c,end=' ')
        a = b 
        b = c
    print()
    print("Sum :",s)
else:
    print("Enter the number of terms less than 13.")