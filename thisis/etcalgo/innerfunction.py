# eval
result1=eval("(3+5)*7") #string으로 들어와도 계산 값 출력
print(result1)

# itertools
## 반복되는 데이터를 처리하는 기능을 포함하는 라이브러리
### itertools을 사용한 순열
from itertools import permutations

data1=[1,2,3,4]

result2=list(permutations(data1, 3))   # 4P3

print(result2, ' ')
print(len(result2)) # 요소의 갯수 24가지

from itertools import combinations

result3=list(combinations(data1, 3)) #4C3

print(result3)
#collection

# heapq
## 우선순위 queue를 위해