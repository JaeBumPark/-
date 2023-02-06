#반복문
"""""
a=range(1,11) #1부터 11-1=10까지 list
print(list(a))

i=10
while i>=1:
    print(i) 
    i=i-1

i=1
for i in range(1,11):
 print(i)

l=1
for l in range(1,11):
    print(l)
    if l>15:
     break
else:
    print(11)
    
#반복문 문제 1. 홀수 출력
x = 20
for i in range(1, x+1):
   if i%2==1:
      print(i)
      """
#반복문 문제 2. 숫자들의 합

y= 10
Sum =0
for i in range(1, y+1):
    Sum=Sum+i
print(Sum)

#반복문 문제 3. 약수출력

z = 6

for i in range(1,z+1):
    if z%i==0:
        print(i, end=' ')
  
