
import sys
input = sys.stdin.readline

N,K=map(int, sys.stdin.readline().split())   # 멀티탭 구멍개수, 사용횟수
L=list(map(int, sys.stdin.readline().split()))
code = []
answer = 0
priority = []

for i in range(K):
    if L[i] in code :  # 코드에 이미 꽂혀져있음
        continue

    if len(code)  !=  N :  # 코드 자리 남음
        code.append(L[i])
        
    for c in code:  # 꽂혀져 있는 코드들
        if c in code[i:]: # 다음에 또 이용해야한다면
            priority.append(code[i:].index(c))
        else:
            priority.append(101)
