
## 백준 채점 시스템에서 최대 재귀 깊이를 디폴트 값으로 1000으로 정해놓음
##런타임 에러는 그 최대 깊이를 초과하여 재귀 호출을 하기 때문에 발생

import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
input = sys.stdin.readline

def dfs(x, y):
    dx = [0, 0, -1, 1]  # 상하좌우 움직임
    dy = [1, -1, 0, 0]  # 상하좌우 움직임

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1  # 방문한 곳은 -1로 표시
            dfs(nx, ny)  # 재귀적으로 DFS 호출

t = int(sys.stdin.readline)  # 테스트 케이스의 수
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline.split())  # 가로, 세로, 배추 개수
    graph = [[0 for _ in range(m)] for _ in range(n)]  # 2차원 배열 초기화

    # 배추 위치 표시
    for _ in range(k):
        X, Y = map(int, input().split())
        graph[Y][X] = 1  # 배추 위치를 1로 표시

    count = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:  # 배추를 발견하면
                dfs(a, b)  # DFS 호출
                count += 1  # 그룹 수 증가

    print(count)  # 그룹 수 출력
