import heapq

#python heap 구현

def heapqueue(iterable):
    h= []
    result = []
    #모든 원소를 heap에 삽입
    for values in iterable:
        heapq.heappush(h, values) # heapq에 iterable value를 쏵다 삽입
    for _ in range(len(h)): # result h의 길이(갯수 만큼) h(heap이라고 가정)에 pop한것 append
        result.append(heapq.heappop(h))
    
    return result

print(heapqueue([9, 14, 53 ,4, 2, 563, 3]))

def maxheapsort(iterable):
    h = [] # heapq
    result= []
    # 모든 원소를 heap에 부호를 바꿔서 삽입
    for values in iterable:
        heapq.heappush(h, -values) 
    for _ in range (len(h)):
        result.append(-heapq.heappop(h))    
    return result

print(maxheapsort([9, 14, 53 ,4, 2, 563, 3]))    
        