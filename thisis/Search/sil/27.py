
#### 선형탐색!!
n,m =map(int, input().split())

l=list(map(int, input().split()))

result=0
for i in l:
    if i==m:
       result+=1
       
print(result)       