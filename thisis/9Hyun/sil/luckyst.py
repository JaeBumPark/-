n= input()

x  = 0
y  = 0
for i in range(len(n)//2):
    x += int(n[i])
for j in range(len(n)//2, len(n)):
    y += int(n[j])    
    
if x == y:
   print("LUCKY!") 
else:       
   print("FUCKYOU") 
   
   
 # n = list(map(int, input()))  