# 이분 검색
def Count(len):  #
    cnt = 0
    for x in L:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
L = []  # 랜선들이 쳐 들어갈 list
res = 0  # Result, 최종값
largest = 0  # 가장 긴 랜선의 길이가 들어갈 변수

for i in range(k):
    tmp = int(input())
    L.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:  # lt가 rt 보다 커지면 탈출!
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1  # while문 탈출!
    else:
        rt = mid - 1
print(res)
