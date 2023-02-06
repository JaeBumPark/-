n, m, k = map(int, input().split())
data= list(map(int, input().split()))
data.sort()
CT=data[n-1]
NCT=data[n-2]
result=0
# for i in range(int(m/k)):
#     CT2 = CT*k
# for j in range(m%k):
#     NCT2 = NCT*(m%k)
# CT2 *= int(m/k)    

# print(CT2)
# print(NCT2)
while True:
    for i in range(k):
        if m == 0:
           break 
        result+=CT
        m -= 1
    if m == 0:
        break
    result+=NCT
    m -= 1
print(result)       