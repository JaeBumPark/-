##이중 반복!
##1292
# import sys

# M,N = map(int, sys.stdin.readline().split())
# L=list()
# for i in range(1, N+1):
#     for j in range(i):
#         L.append(j)

# print(L)    


a, b = map(int, input().split())

sq = []

for i in range(1, b+1):
  for j in range(i):
    sq.append(i)

result = sum(sq[a-1:b])

print(sq)
