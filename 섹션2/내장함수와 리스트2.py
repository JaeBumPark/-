a=[23, 12, 36, 53, 19]
# print(a[:3], "index 0~2 값 출력")
# print(a[1:4], "index 1~3값 출력")

#반복문
# for x in a:
#     print(x, end=' ')
# print()    
# for x in enumerate(a):
#     print(x, "튜플형으로 바꿔수 출력")
    
# b=[1,2,3,4,5] #튜플형으로 출력
# print(b[3]) # 튜플의 3번째 index의 값 출력
#튜플은 값 변경 불가능!!!!

for x in enumerate(a):
    print(x[0], x[1]) # 튜플 a의 index와 value 출력
print()    

for fd, sd in enumerate(a):  
    print(fd, sd) # 요렇게도 가능
    
    