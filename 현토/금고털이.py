W, N = map(int,input().split())

steal_list=[]

for _ in range(N):
    M,P = map(int, input().split())
    steal_list.append([M,P])

steal_list.sort(key=lambda x:x[1], reverse=True) #가격에 따라 정렬
total = 0
for M,P in steal_list:
    if W >= M:
       total += M*P
       W -=  M
    else:
       total += W*P
       break
   
print(total)       