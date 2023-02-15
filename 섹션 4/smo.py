n = int(input())
smo = []
for i in range(n):
    l, w = map(int, input().split())
    smo.append((l, w))
smo.sort(reverse=True)
# print(smo)
cnt = 0  # 대회 나갈 수 있는 명 수
mx = 0  # 최대 몸무게
for l, w in smo:
    if w > mx:
        mx = w
        cnt += 1

print(cnt)
