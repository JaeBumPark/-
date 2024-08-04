# 4
# 2 1 1 0
# 4 2 1 3
N= int(input())
H= list(map(int, input().split()))
ans = [0]*N
for i in range(1, N+1):
    t= H[i-1]
    