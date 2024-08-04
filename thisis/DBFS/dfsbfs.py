from collections import deque

# ##DFS!
# visted = [False]*9 # visted는 방문 처리용 1*9 list
# print(visted)

# def dfs(graph, v, vistied): #graph는 각 node별 인접한 노드(갈수 있는 node),
#     visted[v] = True
#     print(v, end= ' ') # 
#     for i in graph[v]:
#         if not vistied[i]: ## Vistied가 False라면
#            dfs(graph, i, visted)

# graph = [[], [2,3,8], [1,7], [1,4,5], [5], [3,4], [7], [2,6,8], [1,7]]   

# dfs(graph, 1, visted)


##BFS


# def bfs(graph2, start, visited):
#     queue = deque()
#     #현재 Node를 방문 처리    
#     visited[start] = True  
#     # 
#     while queue:
#         # 큐에서 원소 하나 뽑아서 출력
#         v=queue.popleft()
#         print(v, '')
#         for i in graph2[v]: # graph2안의 
#             if not visited[i]:
#                queue.append(i)  
# graph2 = [[], [2,3,8], [1,7], [1,4,5], [5], [3,4], [7], [2,6,8], [1,7]]   

# visited = [False]*9
# bfs(graph, 1, visited)
queue =deque([1])
v= queue.popleft()


graph2 = [[], [2,3,8], [1,7], [1,4,5], [5], [3,4], [7], [2,6,8], [1,7]]   
for i in graph2[v]:
    print(i)
