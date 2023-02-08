
n=int(input())
a=[list(map(int, input().split()))for _ in range (n)]
s=e=n//2
sum=0
# for x in a:
#     print(x)

for i in range(n):
    for j in range(s,e+1):
      sum+=a[i][j]   
 
    if i<n//2:
       s=s-1
       e=e+1   
    else:
       s=s+1
       e=e-1
print(sum)         