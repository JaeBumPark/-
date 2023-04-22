n= int(input())
x = 1 # 시작 좌표
y = 1
plans = input().split()

dx = [0,0,-1,1] #L, R, ,U, D
dy = [-1,1,0,0] # L, R, U, D
moving_type = ["L", "R", "U", "D"]
for plan in plans: #이동 Plan중
    for i in range(len(moving_type)): #moving type 중에
        if plan == moving_type[i]:  # plan과 moving type이 같을경우
           nx = x + dx[i] # 이동 예상 경로는 각 plan별로 움직임
           ny = y + dy[i]
    if nx < 1 or ny < 1: # 만약 이동 예상 경로가 좌표를 벗어난다면?
       continue # (뒤의 코드를 무시하므로) 이동 X
   
    x = nx
    y = ny       

print(x, y)        