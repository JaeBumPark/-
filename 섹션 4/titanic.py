# from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
a.sort()

while a:
    if len(a) == 1:
       cnt+=1 
       break
   
    if a[0]+a.pop[-1] > k:
       a.pop()
       cnt+1
    else:
       a.pop(0)
       a.pop()
       cnt+=1     
       
# pop?
# list = [98, 5123, 432, 24, 55]
# list.pop(0) # 첨꺼 뺌
# list.pop(-1) # 끝거 뺌
# print(list)
