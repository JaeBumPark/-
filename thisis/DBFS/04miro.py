from collections import deque

N, M = int(input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    
dx = [-1,0,1,0] # 북, 동, 남 ,서
dy = [0,1,0,-1]  

def bfs(x, y):
    queue=deque() # queue 설정
    queue.append((x,y))
    while queue:
        x, y = queue.popleft() # queue에서 원소하나 뽑아줌
        # 현재 위치(처음 0,0)에서 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny <0 or ny  >=M: #만약 공간을 넘어간다면?
               continue #해당 이동 무시
            if graph[nx][ny] == 0: #괴물이라면?
               continue #해당 이동 무시
           
            if graph[nx][ny] == 1: #갈 수 있는 공간이라면
               graph[nx][ny] = graph[x][y] + 1 #현재 노드위치의 값 + 1
               queue.append(nx,ny)
    return graph[N-1][M-1]  #마지막 노드의 값 return

bfs(0,0)         
                
# Q = deque()          
# Q.append(8)
# Q.append(5)
# Q.append(7)
# v=Q.popleft()
# print(Q, v)