#WAP to check palindrome using function.
def palindrome(n):
    a = n[::-1]
    print("Reversed string is : ",a)
    if a == n:
        return "Entered string is a palindrome."
    else:
        return "Entered string is not a palindrome."

n = input("Enter the string : ")
print(f"Entered string is : {n}")
print(palindrome(n))

