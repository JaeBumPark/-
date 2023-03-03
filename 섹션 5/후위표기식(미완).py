n = input()
stack = []
dab = ''
for i in n:
    if i.isdecimal():  # isdecimal은 숫자인 함수를 판단하는 함수
        dab += i
    else:
        if i == '(':  # 여는 괄호라면
            stack.append(i)  # stack 에다가 append
        elif i == "*" or i == "/":  # *나 /을 만났을때
            while stack and stack[-1] == '*' or stack[-1] == '/':  # stack 맨 끝에 *나 /가 있다면
                dab += stack.pop()  # 앞에꺼 출력
        elif i == "+" or i == "-"
            stack.append(i)

for j in stack:
    dab += stack.pop()

print(dab)
