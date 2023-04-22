## deque
from collections import deque

listtt =[8, 4, 56, 34, 2]
Q=deque(listtt)
Q.pop() # 뒤에서 요소를 뺌 (2가 빠지겠지?)
Q.popleft() # 앞에서  요소를 뺌 ( 8이 빠지겠지?)
Q.append(53) # 뒤에 53을 추가
Q.appendleft(535) # 앞에 535를 추가
print(Q)
print(list(Q)) # list 형으로 변환

#####dictionry

# list5= ["red", "blue", "green", "yellow"]
# D= dict(enumerate(list5)) #list를 index, value 형태인 tuple로 변경
# print(D)

## Counter
###

from collections import Counter

C=Counter(["A", "A", "B", "C", "D","D", "D"])

print(C["A"]) # A가 나온 갯수 
print(C["D"])  # D가 나온 갯수
print(dict(C)) # Coutner class는 나온 횟수, value라는 key-value 형태를 가짐으로 dictonary 형태료 표현 가능