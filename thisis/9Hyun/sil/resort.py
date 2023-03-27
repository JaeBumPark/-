S=list(input())
num=0
strlist=[]
for i in S:
    if i.isalpha():
       strlist.append(i) 
    if  i.isdecimal():
       num+=int(i)
strlist.sort()
strlist.append(str(num))
       
print(''.join(strlist))        
 