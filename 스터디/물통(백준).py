from collections import deque

a, b, c = map(int, input().split())

q = deque()
q.append((0, 0)) # 경우의 수를 담을 큐


visited = [[False] * (b + 1) for _ in range(a + 1)] # 방문 여부 저장, 중복 방지
visited[0][0] = True  

answer = []

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))
        
def bfs():
    while q:
        x, y = q.popleft()         # A물통에 있는 물: x, B물통에 있는 물: y, C물통에 있는 물: z
        z = c - x - y
        if x == 0:
            answer.append(z)          # A 물통이 비어있는 경우에 C 물통에 남아있는 양 저장

            
        water = min(x, b - y)
        pour(x - water, y + water)         # A에서 B로 물 이동

        water = min(x, c - z)         # A에서 C로 물 이동

        pour(x - water, y)
        
        water = min(y, c - z)         # B에서 C로 물 이동

        pour(x, y - water)
        water = min(y, a - x)          # B에서 A로 물 이동
        pour(x + water, y - water)
        
        water = min(z, a - x)          # C에서 A로 물 이동
        pour(x + water, y)
        
        water = min(z, b - y)         # C에서 B로 물 이동
        pour(x, y + water)
        
bfs()

answer.sort()
for i in answer:
    print(i, end=" ")
