import sys

N,K = map(int, input().split())
S = list(map(int, input().split()))

for i in range(K):
    A, B = map(int, input().split())
    total = sum(S[A-1:B])
    avg = total/(B-A+1)
    print("%.2f" % round(avg, 2))s