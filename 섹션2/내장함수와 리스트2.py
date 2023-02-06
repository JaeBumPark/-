a=[23, 12, 36, 53, 19]
# print(a[:3], "index 0~2 값 출력")
# print(a[1:4], "index 1~3값 출력")

#반복문
for x in a:
    print(x, end=' ')
print()    
for x in enumerate(a):
    print(x)