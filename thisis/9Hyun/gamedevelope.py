n, m = map(int, input().split()) #맵의 크깅
# a=[list(map(int, input().split())) for _ in range(n)] #2차원 배열!
x , y , direction = map(int, input().split())
d = [[0]*m for _ in range(n)]  # 4X4 0 list , 방문한 위치를 정하기 위함
d[x][y] == 1

array=[] # 현재 바다. 위치 상황 
for i in range(n):
    array.append(list(map(int, input().split())))

dx=[-1,0,1,0] #북, 동, 남, 서
dy=[0,1,0,-1]


def turn_left():
    global direction
    
    if direction == 0:
       direction = 3
    else:
        direction -= 1
        
## direction은 0,1,2,3 순서대로 북, 동, 남, 서        
        
## 본게임 시작
count = 1 # 이동한 칸 수
turn = 0 # turn 한 횟수

while True:
  turn_left() # 한 바꾸 돌아
  nx = x+ dx[direction] # 이동하고, 현재 있는 좌표, # direction이 이동의 index
  ny = y+ dy[direction]           
  
  if array[nx][ny] ==0 and d[nx][ny] == 0: #이동할 곳이 들른곳이 아니고, 육지면
     d[nx][ny] = 1 # 이동하니까 방문했다고 1표시하고
     x = nx # 캐릭터의 좌표를 변경(이동)
     y = ny # 마찬가지!
     count += 1 # 방문 칸 횟수를 1 더하고
     turn = 0 # 0으로 회전 횟수 초기화 하고
     continue
 
  else:    #이동할 곳이 없으면           
    turn += 1 # 회전후 다시 while문 처음으로..
    
  if turn == 4:      
     nx = x - dx[direction] # 방향 반대로(뒤로) 가게 "설정"하기
     ny = y - dy[direction] 
     if array[nx][ny] == 0: # 뒤로 갈수 있다면,
        x = nx
        y = ny
     else:
        break
     turn = 0 
     
print(count)         
#방향 설정    
