n,m= map(int, input().split())
l=[]
lt=0
rt=n-1
mid=(lt+rt)//2
for i in range(n):
  l.append(i)
l.sort()

while lt<=rt: