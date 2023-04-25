from collections import deque

##stack

stack=[]

stack.append(3)
stack.append(5)
stack.append(7)

print(stack)
print(stack[::-1]) # 역순으로 출력

queue=deque()

queue.append(3)
queue.append(5)
queue.append(7)
queue.pop()
queue.popleft()
queue.appendleft(12)
print(queue)
print(list(queue)) # list 자료형으로 변경

##재귀 함수

def recursive_function(i):
    if i == 100:
       return
    print() 