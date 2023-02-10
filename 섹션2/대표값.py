
N= int(input())
k=list(map(int,input().split()))
ave= round(sum(k)/N) # 평균 구하기
gaggap=12312
for idx, v in enumerate(k): #튜플값으로 변경
    tmp=abs(v-ave)
    if tmp < gaggap :
        gaggap = tmp
        score = v
        res = idx + 1
    elif tmp == gaggap:
         gaggap = tmp 
         score = v
         res = idx + 1 
         
print()          
# /와 //의 차이?

#/은 나누기로 나온 결과값을 소수점까지 출력한다. // 정수 나눗셈을 하는 연산자로 소수점 아래를 버리고 정수값만 보여준다.