n = int(input())
array = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
res = "" ##L, R 적기
tmp = []

while lt>rt: