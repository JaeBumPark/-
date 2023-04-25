d = [0] * 100 # 계산 결과 저장 // 피보나치의 각 index별 값
## top-down
def fibo(x):
    if x == 1 or x == 2:
       return 1
    if d[x] != 0: # 계산한 적이 있으면
       return d[x]  #그대로 반환
    d[x] = fibo(x-1) + fibo(x-2)
    
    return d[x]
print(fibo(5))    

## Bottom-up

d2 = [0]*100

d2[1] = 1
d2[2] = 1
n = 99

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2] 
    
print(d[n])    