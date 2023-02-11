n=int(input())
a=list(map(int, input().split()))  #input()은 사용자가 입력하는함수
max=-12341212

def digit_sum(x):
    sum=0
    while x>0:
      sum=sum+x%10 #내머지
      x=x//10 #몫
    return sum  # 자릿수의 합


for x in a : #a list의 있는 값들 중에
    tot=digit_sum(x)
    if tot > max:
       max= tot  #가장 큰 자리수의 핪
       res = x # 자리수의 합이 가장 큰 숫자
print(res)
