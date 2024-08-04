
from collections import deque
# n, m =map(int, input().split())
# dq= [(index, val) for index,val in enumerate(list(map(int,input().split())))]# enemerate 함수!
# dq=deque(dq)
# cnt = 0
# while True:
 
#   curr=dq.popleft() #(맨 앞에 존재하는 list 한개)
#   if any(curr[1]<x[1] for x in dq):  ##위험도
#      dq.append(curr)

#   else:
#      cnt += 1
#      if curr[0]==m:
#         print(cnt)
#         break
         
n,m = map(int, input().split())


#### enumerate()