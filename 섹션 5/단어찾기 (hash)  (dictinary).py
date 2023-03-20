#dictonary 단어 
n=int(input())
p= dict()
for i in range(n):
    a = input() # input으로 단어를 넣고
    p[a]=1 # 현재 들어간 단어의 value값은 1이다!!!
for j in range(n-1):
    b= input()
    p[b]=0  #현재 들ㅇ거단 단어의 value값은 0으로 변경!!      

print(p)
for key,values in p.items() :
    if values==1:
       print(key)
       break