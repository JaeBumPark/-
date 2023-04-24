N= int(input())

scary = list(map(int, input().split()))
scary.sort()
team = 0
count = 0 # 모험가의 수

for i in scary:
    count += 1
    if count >= i:
       team += 1
       count =0
       
print(team)        