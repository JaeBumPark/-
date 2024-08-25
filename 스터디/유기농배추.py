
## 백준 채점 시스템에서 최대 재귀 깊이를 디폴트 값으로 1000으로 정해놓음
##런타임 에러는 그 최대 깊이를 초과하여 재귀 호출을 하기 때문에 발생

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  ##최대 깊이 limit을 위해

def dfs(x, y): # dfs 정의

    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]      # 상하좌우

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1         # 범위 안에 있고 1이면(=배추이면) 지나간것을 -1로 표시하고 주변 탐색
            dfs(nx, ny)

t = int(sys.stdin.readline()) # 테스트 케이스의 개수
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    graph = [[0 for _ in range(m)] for _ in range(n)]

    # 배추 위치 표시
    for _ in range(k):
        X, Y = map(int, input().split()) 
        graph[Y][X] = 1 # X, Y 바꿔서 표시해야하는거 주의!

    # 배추 그룹 수(=배추흰지렁이 개수) 세기
    count = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a ,b)
                count += 1
    print(count)
