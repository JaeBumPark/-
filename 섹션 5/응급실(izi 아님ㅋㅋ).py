
from collections import deque

n, m =map(int, input().split())
dq=[(index, value) for index, value in enumerate(list(map(int, input().split())))]# 딕셔너리 자료형!!
dq=deque(dq)  #deque랍니다~
cnt=0
while True: # 계속해서 도는데,
   cur=dq.popleft()
   if any(cur[1] < x[1] for x in dq):
      dq.append(cur)
   else:
      cnt += 1
      if cur[0] == m:
         print(cnt)
         break





#### enumerate()