a = [23, 12, 36, 53, 19]

print(a[0:5:2])

###
for x in enumerate(a): ## enumerate? tuple값으로 출력됨 / index와 index의 해당 값이 출력
    print(x)
    
for x in enumerate(a): 
    print(x[0], x[1])  
    
for index, value in enumerate(a):
    print(index, value)    
    
if all(60 > x for x in a):
   print("YES!")     
   
if any(60>x for x in a): 
   print("YES!")   