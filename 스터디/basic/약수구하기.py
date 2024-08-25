import sys

M, N = map(int, sys.stdin.readline().split())
L = []
for i in range(1, M + 1):
    if M % i == 0:
        L.append(i)

if len(L) >= N:
    print(L[N-1])
else:
    print(0)  # 또는 -1로 변경 가능
