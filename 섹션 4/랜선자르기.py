# 이분 검색
k,n = map(int, input().split())
array = []

for i in range(4):
    lan = int(input())
    array.append(lan)
    largest = max(largest, lan)
    
    
lt =1     
rt = largest 
mid = (lt+rt)//2

while lt <= rt 