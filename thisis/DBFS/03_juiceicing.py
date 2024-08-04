# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
ice_board = []
for i in range(n):
    ice_board.append(list(map(int, input())))

# 상하좌우 진행용 방향 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아이스크림 개수
count = 0

# dfs를 통해 현재 노드를 방문한 뒤, 연결된 모든 노드들을 방문
def dfs(start_x, start_y):

    # 현재 노드를 방문 처리
    ice_board[start_x][start_y] = 1

    # 현재 노드와 인접한 모든 노드들을 탐색하며, 방문 가능할 경우 방문
    for i in range(4):

        # 인접 노드 좌표
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        # 인접 노드가 얼음판 내부에 위치할 경우
        if (nx >= 0 and nx < n and ny >= 0 and ny < m):

            # 인접 노드에 음료수를 채울 수 있는지 확인
            if (ice_board[nx][ny] == 0):

                # 인접 노드 방문
                dfs(nx, ny)

# 모든 위치에 음료수 채우기
for i in range(n):
    for j in range(m):
        # 해당 노드에 음료수를 채울 수 있다면
        if (ice_board[i][j] == 0):
            # 해당 노드에서 dfs 탐색 시작
            dfs(i,j)
            count += 1

print(count)