
n= int(input())
reward=0  #상금 계싼
maxi=0   # 가장 큰 상금
for i in range(n):
    tmp=input().split() # 여러값을 받아서 sort할때는 이렇게 변수 선언 해놓고
    tmp.sort() # sort~!
    a,b,c = map(int, tmp)
  
    if a == b and b == c:#if 문을 쓸때는 가장 좋은것을 if에 써야함!!
       reward= 10000+ a*1000
    elif a==b:
       reward= 1000+a*100
    elif b==c:
       reward= 1000+b*100 
    elif a==c:
       reward= 1000+c*100   
    else:
       reward=c*100
    if reward>maxi:   # 현재 상금이 가장 큰 상금 보다 클경우
       maxi=reward     # 가장 큰 상금을 갱신
print(maxi)       