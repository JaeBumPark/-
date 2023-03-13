import heapq

def heapsort(x):
    h =[]
    result = []
    for i in x:
        heapq.heappush(h, i) # 모든 원소를 h(heap)에 삽입
    for j in range(len(h)):
        result.append(heapq.heappop(h)) # reulst에 heap에서 pop 한 값들 append
    return result
result = heapsort([5, 3, 621345, 3 ,4, 5, 3])
print(result)
      