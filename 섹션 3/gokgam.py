n = int(input())
list1= [list(map(int, input().split()))for _ in range (n)]
m= int(input())

# print(list1[1])
# print(list1[1])
for i in range (m):
    h, d, r = int(input().split())
    if d == 0:
       list1[h-1].append(list1[h-1].pop(0))
    else:
       list1[h-1].insert(0,list1.pop(-1)) 
       
for i in range(n):
    for j in range(s,e+1):
      sum+=a[i][j]   
 
    if i<n//2:
       s=s-1
       e=e+1   
    else:
       s=s+1
       e=e-1