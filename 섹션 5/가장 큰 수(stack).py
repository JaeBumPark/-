
n, m=map(int, input().split()) #숫자 2개를 받고
n=list(map(int, str(n))) #n에서 받은 숫자를 str으로 받고->int형으로 변경후, list화
print(n)
stack= []
for x in n:
  while stack and m>0 and stack[-1]<x:
    stack.pop()
    m-=1
  stack.append(x)
# if m!=0: #m을 다 안했을경우, 요런문제가..!
#   stack=stack[:-m] #슬라이싱! -m번째 배열 전까지!

# print(stack)
for x in stack:
    # print(x, end='') #공백없이 출력! or
  res=''.join(map(str, stack))
print(res)