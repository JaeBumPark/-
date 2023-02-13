# 이분 검색
def Count(len):  #

    return cnt


N, M = map(int, input().split())
L = []  # 랜선들이 쳐 들어갈 list

res = 0
largest = 0  # 가장 긴 랜선의 길이가 들어갈 변수
lt = 1
rt = largest
for i in range(N):
    tmp = int(input())
    L.append(tmp)
    largest = max(largest, tmp)
while lt <= rt: # lt가 rt 보다 커지면 탈출!
      mid= (lt+rt)//2
      if Count(mid) >= n:
