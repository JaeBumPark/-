n= int(input())
l= [list(map(int, input().split() )) for _ in range(5)]
m= int(input())

for i in range(m):
    x,y,z = map(int, input().split())
    if y == 0:
       for _ in range(z):
         l[x-1].append(l[x-1].pop(0)) #z번 만큼 해당 열의 맨 앞 요소를 빼서 뒤에 추가
    else: 
       for _ in range(z):
         l[x-1].insert(0, l[x-1].pop())     
s=0
e=n-1
sum=0                                                                                                                  
for i in range(n):         
      for j in range(s,e+1):
          sum+=l[i][j] 
      if i < n//2:    
          s+=1
          e-=1    
      else:
          s-=1
          e+=1         
print(sum)          


#pop, append, insert
# a= [8, 3, 5, 7, 9]
# a.insert(1, 11) #1번 index에 1을 넣어버리겠다!
# print (a, "1번 index에 11 넣어버렷!")
# a.pop()
# print (a, "9 빼버렷!")
# a.pop(0)
# print(a, "8 빼버렷!")

