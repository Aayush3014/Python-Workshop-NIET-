string = input("Enter the sentence : ")

str_list = string.split()

str_list.sort(key=len) 

print(str_list[-1])