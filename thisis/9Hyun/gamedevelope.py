n, m = map(int, input().split())
# a=[list(map(int, input().split())) for _ in range(n)] #2차원 배열!
d = [[0] * m for _ in range(m)]  # 4X4 0 list
x, y, lo = map(int, input().split())  # 현재 좌표(x,y), 바라보는 방향 lo
d[x][y] == 1 # 현재 위치를 방문처리(1로 채움)
array = []  # 현재 맵을 담을 빈 list
for i in range(n):
    array.append(list(map(int, input().split())))

print(array)
