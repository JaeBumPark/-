n=int(input())
l = [list(map(int, input().split())) for _ in range (n)] #2차원 리스트
dx=[0,0,-1,1]  #상, 하, 좌, 우 
dy=[-1,1,0,0]

l.insert(0,[0]*n) #2차원 list 0번 인덱스에 n 갯수만큼 0으로 이루어진 LIST 추가
l.append([0]*n) # 2차원 LIST마지막에  n 갯수만큼 0으로 이루어진 LIST 추가
for x in l: # 2차원 LIST 별 각 구성요소 LIST에
    x.insert(0, 0)
    x.append(0)
cnt=0 # 봉우리 갯수
    
for i in range(1, n+1):# i는 행
    for j in range(1, n+1):              #j는 열
        if all(l[i][j] > l[i+dx[x]][i+dy[x]] for x in range(4)):
           cnt +=1 
           
print(cnt)            