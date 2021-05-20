#WAP to compute GCD of two numbers using function. 
def hcf(num1,num2):
    if num1>num2:
        greater = num1
    else:
        greater = num2
    while greater>0:
        if num1%greater==0 and num2%greater==0:
            return f"GCD of {num1} and {num2} is {greater}."
        else:
            greater-=1

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(hcf(num1,num2))
