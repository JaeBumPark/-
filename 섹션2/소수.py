N=int(input())
ch=[0]*(N+1)
cnt=0 #소수의 갯수
for i in range(2, N+1):
    if ch[i] == 0: # 0이라면 소수라고 가정했으므로
       cnt+=1 # cnt 1개 추가
       for j in range (i, N+1, i): #i부터 N까지 i만큼 증가시켜서(i만큼 증가시키면 i의 배수 임으로 소수 ㅌ
          ch[j] = 1 # 1로 바꿔서 소수가 아님을 표현
print(cnt)
