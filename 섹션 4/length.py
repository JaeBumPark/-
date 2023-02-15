l = int(input())
x = list(map(int, input().split()))
m = int(input())  # 길이 조정 갯수
x.sort()  # 정렬

for _ in range(m):
    x[0] += 1
    x[l-1] -= 1
    x.sort()

print(x[l-1]-x[0])
