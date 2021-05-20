#Python program to solve Quadritic equation.

import cmath
def quad():
    a=float(input("Enter First Number: "))
    b=float(input("Enter second Number: "))
    c=float(input("Enter third Number: "))

    d = (b**2) - (4*a*c)

    x = (-b+cmath.sqrt(d))/(2*a)
    y = (-b-cmath.sqrt(d))/(2*a)
    return f'The solution of given Quadritic Equation \n {x} \n {y}'

print(quad())