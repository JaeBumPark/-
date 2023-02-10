
N, M = map(int, input().split())  #map함수에 대해 알아보기!

cnt=[0]*(N+M+2) #눈의 합 합계를 기록할 list

max= -241234531251212

for i in range (1,N+1):
    for j in range (1,M+1):
        cnt[i+j]+=1 #[i+j] index에 있는 리스트 값 = 나온 합의 값!!
for i in range (N+M+1):
    if cnt[i]>max:
        max = cnt[i]
for i in range (N+M+1):
    if cnt[i] == max:
        print(i, end = ' ')        
        
            