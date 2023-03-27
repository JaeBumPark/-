##이코테 실전 9hyun resort.py
#join 함수: list의 값들을 하나하나 출력해줌
# list1=["A", "B", "C", "D", "E"]
# print(''.join(list1))

# isdecimal(), isalpha()
##isdecimal()은 숫자만 판별, isalpha()는 알파벳만 판별

# S=list(input())
# for i in S:
#     if i.isalpha():
#        print(i, "알파")
#     if i.isdecimal():
#        print(i, "숫자") 

##이코테 실전 sort 23KES.py

# key=lamdba

list=[]

for i in range(3):
    [a, b, c, d] = map(str, input().split())
    
    list.append([a, int(b), int(c), int(d)])
    
sorted=sorted(list, key=lambda x: (len(x[0])))
print(sorted)