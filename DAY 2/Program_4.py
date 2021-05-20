# WAP to print sum of series.
import math
def sumofseries(n):
    sum = 0 
    num = 0
    fact = 1
    for i in range(1,n+1):
        num+=1
        fact+=1
        sum += (num)/math.factorial(fact)
    return sum
n = int(input("Enter number of terms : "))
print("Sum of series : ",sumofseries(n))