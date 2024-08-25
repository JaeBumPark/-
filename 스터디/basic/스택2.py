import sys

N = int(sys.stdin.readline()) # 명령의 수 입력 받기
ST = [] # 스택 초기화
for i in range(N): # 5가지의 명령에 대해서 코드 작성
    op = sys.stdin.readline().split() # 1 42 입력하면 ['1', '42']
    if op[0] == '1':
        ST.append(int(op[-1]))
    elif op[0] == '2':
        if ST:
            print(ST.pop(-1))
            continue
        print(-1)
    elif op[0] == '3':
        print(len(ST))
    elif op[0] == '4':
        if ST:
            print(0)
            continue
        print(1)
    elif op[0] == '5':
        if ST:
            print(ST[-1])
            continue
        print(-1)
              