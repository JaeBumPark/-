n,m =map(int, input().split())
cnt = 0 #연산 횟수
while n > 1:
   if n % m == 0:
      n=n//m
      cnt+=1
      print(n, "case 1")
   else:
      n-=1
      cnt+=1
      print(n, "case 2")
print(cnt)

