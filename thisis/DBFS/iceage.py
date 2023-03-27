n,m=map(int, input().split())
graph = [list(map(int, input())) for _ in range (m)]
result = 0

def BFS(x, y):
    if x<=-1 or x >=n or y<=-1 or y>=m:
       return False # 틀 범위를 초과할 경우 Fasle
   