n = input()
result=[]
value = 0

for i in n:

    if i.isalpha():
       result.append(i)
    else: 
       value += int(i)
   
result.sort()
result.append(str(value))



print(''.join(result))              