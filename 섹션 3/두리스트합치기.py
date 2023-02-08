n= int(input())
a= list(map(int, input().split()))
m= int(input())
b= list(map(int, input().split()))
d=list()
# p1=0 #3일경우 2까지 가능
# p2=0 #5일경우 4까지 가능
# c=list()

# while p1 < n and p2 < m:  
#     if a[p1]<=b[p2]:
#         c.append(a[p1])
#         p1+=1
#     else:
#         c.append(b[p2])
#         p2+=1
# #남은 리스트의 값들을 c에 추가
# # if p2<m:
# #    c.append(b[p2:]) #슬라이싱을 이용하여 남은 리스트 값들을 c에 추가 
# # if p1<n:
# #    c.append(a[p1:])  # 이랬더니 list 처럼 추가되넹... 
# if p2<m:
#    c=c+b[p2:] #슬라이싱을 이용하여 남은 리스트 값들을 c에 추가 
# if p1<n:
#    c=c+a[p1:]  # 이랬더니 list 처럼 추가되넹... 
# print(c)        

# for x in c:
#     print(x, end = '  ')
d= a+b
d.sort()
print(d)