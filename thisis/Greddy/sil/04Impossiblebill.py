N = int(input())
array = list(map(int, input().split()))
array.sort()
for i in array:
    target = 1
    
    if target < i:
       break
    target += i # target을 하나씩 늘려가며 확인!
            
        