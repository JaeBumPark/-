n= int(input())
# dy=[list(map(int, input().split())) for _ in range (n)] 2차원 list
dy=[0]*(n+1)
print(dy)
dy[1]==1
dy[2]==2
for i in range(3, n+1):
    dy[i] == dy[i-2] + dy[i-1]
    