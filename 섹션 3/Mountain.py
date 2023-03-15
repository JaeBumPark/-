n=int(input())
l = [list(map(int, input().split())) for _ in range (n)]
dx = [-1, 0, 1, 0] # 좌, 우 이동
dy = [0,1, 0, -1] # 상, 하 이동
cnt=0
l.insert(0, [0]*n) #2차원 행렬 첫행으로 [0]*n 박음
l.append([0]*n)    # 2차원 행렬 끝에 [0]
for x in l: # x는 각 행
    x.insert(0,0)
    x.append(0)
    
print(l)    
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(l[i][j]>l[i+dx[k]][j+dy[k]] for k in range(4)):
           cnt += 1

print(cnt)