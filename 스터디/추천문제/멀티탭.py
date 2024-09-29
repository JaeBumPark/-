import sys
input = sys.stdin.readline

# 멀티탭 구멍 개수 N, 전기 용품 사용 횟수 K
N, K = map(int, input().split())
L = list(map(int, input().split()))  # 전기 용품의 사용 순서
code = []  # 현재 멀티탭에 꽂혀 있는 전기 용품
answer = 0  # 플러그를 뽑는 횟수

for i in range(K):
    if L[i] in code:     # 이미 멀티탭에 꽂혀 있는 기기라면 pass
       continue

  
    if len(code) < N:   # 멀티탭에 자리가 남아있다면 새로운 기기를 꽂는다.
        code.append(L[i])
        continue  # 자리가 남아 있을 때는 교체 로직으로 가지 않도록 한다.


    # 멀티탭이 꽉 차있는 경우, 우선순위를 계산해서 가장 늦게 사용되거나 사용되지 않는 기기를 뽑는다.
    priority = []  # 각 코드가 다음에 언제 사용되는지 기록
    for c in code:
        if c in L[i:]:  # 멀티탭에 꽂힌 기기가 앞으로도 사용될 경우
            priority.append(L[i:].index(c))
        else:  # 사용되지 않는다면 매우 큰 값을 넣어 우선적으로 뽑도록 설정
            priority.append(999)

    out_idx = priority.index(max(priority))     # 가장 우선순위가 낮은 기기의 인덱스를 찾는다.
    code[out_idx] = L[i]     # 그 기기를 빼고 새로운 기기를 꽂는다.
    answer += 1

# 최소 플러그를 뽑는 횟수 출력
print(answer)
