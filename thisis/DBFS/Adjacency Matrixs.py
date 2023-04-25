#인접 행렬

INF = 999999

matrix = [ [0,7,5], [7,0,INF], [5,INF,0]] # 0, 1, 2는 각각의 거리가 이렇다.


print(matrix)


#인접 그래프

graph =[[] for _ in range (3)]

# 노드 0에서의 각 노드 별 거리

graph[0].append((1,7)) # 
graph[0].append((2,5)) # 1 노드까지 거리 7, 2 노드까지 거리 5
# 노드 1에서의 각 노드 별 거리
graph[1].append((0,7))

# 노드 2에서의 각 노드 별 거리
graph[2].append((0,5))

##연결 확인
print(matrix[1][2]) #node 1과 2가 연결되어 있을까?

