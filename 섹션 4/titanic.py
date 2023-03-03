from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
a.sort()

while a: # while list? => list가 빌 때 까지 수행!!!!
    if len(a) == 1: # 한명 남았으면
       cnt += 1
       break

    if a[0] + a[-1] > k:
        a.pop()
        cnt += 1
        print(cnt, " 1 case ")

    else:
       a.pop(0)
       a.pop()
       cnt += 1
       print(cnt, " 2 case ")


print(cnt)

# pop?
# list = [98, 5123, 432, 24, 55]
# list.pop(0) # 첨꺼 뺌
# list.pop(-1) # 끝거 뺌
# print(list)
