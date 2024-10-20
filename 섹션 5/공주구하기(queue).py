#queue를 사용하는 문제!


from collections import deque

n, k =map(int, input().split())
dq=list(range(1,n+1)) #복습! 1부터 n까지 list
dq=deque(dq)  #deque랍니다~

while dq:
  for _ in range (k-1):
      lef=dq.popleft() #안빠질새끼들
      dq.append(lef)
  dq.popleft()
  if len(dq) == 1:
     print(dq[0])
     dq.pop()


dq2=list(range(1, 8))
dq2=deque(dq2)
for _ in range(2): (2번 반복!!!)
    dq2.popleft()
print(dq2)
