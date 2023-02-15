n, m = map(int, input().split())
minute_list = list(map(int, input().split()))

hap = 0
res = 0


def Count(capacity):
    cnt = 1
    sum = 0
    for j in minute_list:
        if sum + j > capacity:
            cnt += 1
            sum = j
        else:
            sum += j
    return cnt


for i in minute_list:
    hap += i

lt = 1
rt = hap

while lt < rt:
    mid = (lt + rt) // 2
    if Count(mid) <= m: # 이 용량으로 모자라면??
        res = mid
        # lt = mid + 1
        rt = mid - 1
    else:
        # rt = mid - 1
        lt = mid+1

# for i in range(n):
#     tmp = int(input())
#     minute_list.append(tmp)
print(res)
print(hap)