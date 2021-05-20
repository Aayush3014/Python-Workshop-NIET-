#inverting dictionary

dic = {"name":"Aayush","age":18,"branch":"AI"}
print("Initial Dictionary :",dic)
inv_dic = {v : k  for k,v in dic.items()}
print("Inverted Dictionary :",inv_dic)