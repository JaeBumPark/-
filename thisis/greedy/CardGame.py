n,m =map(int, input().split())
Dab=0

for i in range(n):
    l= list(map(int, input().split()))
    min_value=50000
    for j in l:
        min_value=min(j, min_value)
       
    Dab= max(min_value, Dab)   
     
print("가장 작은수 : " , Dab)