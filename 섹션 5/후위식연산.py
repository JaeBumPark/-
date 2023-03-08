n=input()
stack=[]
dab=0

for i in n:
    if i.isdecimal():
       stack.append(i)
    else:
      if x == "+":  
        n1=stack.pop()     
        n2=stack.pop()
        stack.append(n1+n2)
      
      