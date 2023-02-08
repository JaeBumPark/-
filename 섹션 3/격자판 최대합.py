n=int(input())
a=[list(map(int, input().split())) for _ in range(n)] #2차원 배열!

largest = -21470000
sum3=sum4=0
for i in range(n):
    for j in range(n):
        sum1=sum2=0
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest= sum1
    if sum2>largest:
        largest= sum2
print(largest)
for i in range(n):
        sum3+=a[i][i]
        sum4+=a[i][n-i-1]
if sum3>largest:
    largest= sum3
if sum4>largest:
    largest= sum4    
    
    
print(largest)          
             
        
#변수 위치 잘 확인