from itertools import permutations # 순열
from itertools import combinations # 조합
# sum
result1 = sum([1, 2, 3, 4, 5])
print(result1)
# min
result2 = min([423, 2341234, 34])
print(result2)
# sort
result3 = [94, 43, 43, 3, 4]
result3.sort(reverse=True) # 내림차순
print(result3) 

#순열과 조합
#itertools
## Python에서 반복되는 데이터를 처리하는 기능을 가진 library
list4=[1,2,3,4]
result4= list(permutations(list4,3)) # 4P3 
print(result4, ' ')
print(len(result4)) # 순열의 갟수
result5 = list(combinations(list4, 3)) #4C3
print(len(result5))
#heapq
# 다이젝스트라 알고리즘에 사용
# 우선순위 queue
