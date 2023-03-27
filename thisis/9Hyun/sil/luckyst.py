n = list(map(int, input())) # int 형 배열
x=0
y=0
for i in range(len(n)//2):
    x+=n[i]

for j in range(len(n)//2, len(n)):
    y+=n[j] 


if x==y: 
   print("LUCKY")
else:
   print("READY")                      
        