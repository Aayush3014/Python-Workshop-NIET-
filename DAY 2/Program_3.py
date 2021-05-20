# WAP to find prime number from 1 to n.
lower = int(input("Enter the lower number : "))
upper = int(input("Enter the upper number : "))
sum = 0 
for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            sum += i
            print(i,end=' ')
print()
if sum%5==0:
    print("Sum of prime numbers is divisible by 5.")
else:
    print("Sum of prime numbers is not divisible by 5.")