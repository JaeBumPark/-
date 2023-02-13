n, m = map(int, input().split())
# min = 51251235123
# minmax = -1241241 모가 다를까??
for i in range(n):
    min = 51251235123
    minmax = -1241241
    data = list(map(int, input().split()))
    for j in data:
        if j < min:
           min = j
    # minmax = max(minmax, min)
        if min > minmax:
           minmax = min
print("가장 작은수중 가장 큰수 : ", minmax)

# 최대,최솟값 함수는 min,max를 사용하자!
#전역변수 지역변수 차이?!
