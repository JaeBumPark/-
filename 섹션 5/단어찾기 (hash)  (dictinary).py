#dictonary 단어 
n=int(input())
p= dict()
for i in range(n):
    a = input()
    p[a]=1 # 키 값이 1이다!!
for j in range(n-1):
    b= input()
    p[b]=0        

print(p)
for key,values in p.items() :
    if values==1:
       print(key)
       break 