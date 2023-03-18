# # list slicing
# l=[list(map(int, input().split())) for _ in range (4)]
# print(l[1][0::1]) # 4 8 5 2
# print(l[1][1])
# # sum

k=list(map(int, input().split()))
if k == k[::-1]: #회문 검사! 뒤부터 가져옴!!
   print("y")
else:
  print("n")      

print(k[::-1])   
      
#
l[3]