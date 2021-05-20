def printstatus():
    '''This function tells us the marriage status of the person'''
    s = input("Enter status : ")
    if s=="S":
        return "Separated"
    elif s=="M":
        return "Married"
    elif s=="D":
        return "Divorced"
    elif s=="U":
        return "Unmarried"
    else:
        return "Please enter the status from the given categories "
print(printstatus.__doc__)
print(printstatus())
