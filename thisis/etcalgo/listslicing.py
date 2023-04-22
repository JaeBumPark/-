### simple Dijkstra code

INF=int(1e10) # 10억으로 설정


#노드의 갯수, 간선의 갯수를 입력 받기
n,m= map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 node의 거리를 담은 list
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a에서 b번 노드로 가는 비용이 c이다.
    
# print(graph)    
# print(graph[0])
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(index)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
            
def dijkstra(start):
    #tlwkr shemdp eogo chrlghk            