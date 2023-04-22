import heapq

n=int(input())
heap=[] #heap은 빈 리스트
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0
while len(heap) != 1: # heap 길이가 1이 아닐동안만(1이면 끝)
      one=heapq.heappop(heap)
      two=heapq.heappop(heap)
      value = one + two # 중간 합쳐진 카드 뭉치
      result += value
      heapq.heappush(heap, value)
print(result)          
    

# heap2=[]
# heaplist=[]
# for i in range(5):
#     d= int(input())
#     heapq.heappush(heap2, d)
    
# for _ in range(5):
#     heaplist.append(heapq.heappop(heap2))    
# print(heaplist)