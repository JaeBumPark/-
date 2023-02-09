
N, K= map(int, input().split()) #첨에 case 저장
a= list(map(int, input().split())) #list들 저장
res =set() #set자료구조, 중복해서 넣어도 한번만 들어간다!! 중복을 제거한다!
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res(K-1))           

#set 과 add
# set 자료구조는 중복값이 들어가도 한번만 들어감!
# set 자료구조에 추가하기 위해선 add!