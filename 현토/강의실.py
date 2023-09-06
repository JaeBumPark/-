import sys
N= int(sys.stdin.readline())
C = []
for _ in range(N):
    S,F = map(int,sys.stdin.readline().split())
    C.append((S,F))

C.sort(key=lambda x:(x[1], x[0])) 

cnt=0
Ft = 0
for S,F in C:
    if Ft <= S:
       Ft = F
       cnt += 1
print(cnt)       