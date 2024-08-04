
from collections import deque

N, M = map(int, input().split())

board = [0] * 101  # board 판, index별 값은 이동 횟수(굴린 횟수)
visited = [False] * 101  # 방문 한 곳인지 check

ladder = dict()
snake = dict()

for i in range(N):
    a1, b1 = map(int, input().split())
    ladder[a1] = b1

for i in range(M):
    a2, b2 = map(int, input().split())
    snake[a2] = b2

queue = deque([1])  # queue 생성

while queue:
    a = queue.popleft()
    if a == 100:
        print(board[a])
        break
    for d in range(1, 7):  # 주사위 던지기
        next_pos = a + d
        if next_pos <= 100 and not visited[next_pos]:  # 맵 안넘어가고, 방문한 적이 없으면
            visited[next_pos] = True
 
            if next_pos in ladder.keys():  # 사다리 칸에 있으면,

                next_pos = ladder[next_pos]
                visited[next_pos] = True
                board[next_pos] = board[a] + 1
                
            elif next_pos in snake.keys():  # 뱀 칸으로 오면

                next_pos = snake[next_pos]
                visited[next_pos] = True
                board[next_pos] = board[a] + 1
            else:
            #   visited[next_pos] = True  # 방문 처리(사다리도 아니고 뱀도 아닐때)
                board[next_pos] = board[a] + 1
            # if next_pos == 100:  # 목적지에 도착했다면 종료
            #     print(board[next_pos])
            #     exit()
            queue.append(next_pos)
