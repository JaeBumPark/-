#내장함수
import random as r #random? : 
"""
a= []  #빈 list
print(a)
a= [1,2,3,4,5]
print (a)

a.append(6) # append: list에 추가
print (a)

a.insert(3,7) # insert: list의 3번 index에 7을 추가
print (a)

a=list(range(1, 11)) #a 초기화! a는 1부터 11까지들어가있음
r.shuffle(a) #random으로 a를 섞어보아라!
print(a)
a.sort() #a를 오름차순으로 정렬!

print(a.index(5)) #list의 index  출력
#1차원 리스트, 2차원 리스트
"""
# a=[0]*3 #0으로 구성되있는 3개 방을 가진 list 만들기

# a=[[0]*3 for _ in range(3)]
# print(a)

a=[1,2,3,4,5]
b=list(range(1,11))

#pop 
# print(a)

# a.pop()

# print(a)

# a.pop(1)

# print(a)
# remove
# a.remove(4)
# print(a)

# print(a.index(4)) # 4의 index 출력
# print(sum(a), "합")
# print(max(a), "최대값")
r.shuffle(a) # 썩어~
print(a)
a.sort() 
print(a, "오름차순")
a.sort(reverse=True)
print(a, "내림차순")