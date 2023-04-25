n = int(input())
array = []

for i in range(n):
    h, w = map(int,input().split())
    array.append((h,w))
    
array.sort(reverse=True) # 내림차순으로 정렬

cnt = 0 # 답
mx = 0 #최대 몸무게

for h,w in array:
    if w> mx:
       mx = w
       cnt += 1
       
print(cnt)             

