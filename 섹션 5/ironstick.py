n=input()#공백없이 입력
m=list(str(input()))
stack=[]
cnt = 0
for i in range(len(n)): # 괄호의 길이 만큼!
    if n[i] == '(':
       stack.append(n[i])
print(stack)
# print(type(n))
# print(type(m))
# print(type(n[2]))
print(type(stack))
print(n)
print(m)