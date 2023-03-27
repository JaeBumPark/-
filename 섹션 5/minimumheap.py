import heapq as hq

list=[]

hq.heappush(list, 4)
hq.heappush(list, 8)
hq.heappush(list, 11)
hq.heappush(list, 2)
hq.heappush(list, 3)
print(list)
# while True:
#   n= int(input())
#   if n == 0:
#      print(hq.heappop(list))  
#      if len(list) == 0:
#         print(-1)
#   elif n == -1:
#        print(list)
#        break  
   
#   else:
#       hq.heappush(list, n) # list에 n을 최소힙의 형태로 넣음