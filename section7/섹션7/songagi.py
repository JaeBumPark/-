import sys
from collections import deque

S, E = map(int, sys.stdin.readline().split())


MAX = 1000
check = [0]*MAX # 방문했는지 아닌지 check
distance = [0]*MAX # 몇 번 걸리는지 check


check[S] == 1
dq = deque()
dq.append(S)

while dq: #queue가 모두 빌 때 까지
   now = dq.popleft() # 현재 위치를 popleft()로 빼고,
   if now == E:
      break
  
   for next in (now-1, now+1, now + 5):
       if check[next] == 0 :
         dq.append(next)
         check[next] = 1 # 방문처리 해두고,
         distance[next] = distance[now] + 1
       
print(distance[E])             