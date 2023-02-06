# INF= 9999999999

# #2차원 리스트를 이용한 인접 행렬 표현
# graph = [
#     [0,7,5],
#     [7,0, INF],
#     [5,INF,0]
# ]

# print(graph)
# print(graph[1][0])
# #인접 리스트 표현

# graph2 = [[] for _ in range(3)] # 행이 3개인 2차원 리스트로 인접 리스트 표현
# graph2[0].append((1,7)) #0에 연결된 노드 정보 저장
# graph2[0].append((2,5)) #0에 연결된 노드 정보 저장
# graph2[1].append((0,7)) #1에 연결된 노드 정보 저장
# graph2[2].append((0,5)) #2에 연결된 노드 정보 저장
# print(graph2[0])
# print(graph2[1])
# print(graph2[2])
# print(graph2)


#DFS method 정의
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4 ,5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]        
visted = [False] * 9
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            # print(i)
            dfs(graph, i, visited)
        


dfs(graph, 1, visted)
