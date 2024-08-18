from collections import deque

puzzle = ""
for i in range(3):
    puzzle += "".join(list(input().split())) # 퍼즐을 2차원이 아닌 문자열 형태로 정렬


visited_dict = {}  # 빈 딕셔너리 생성
visited_dict[puzzle] = 0  # 퍼즐 상태와 이동 횟수를 key:value로 저장
queue= deque([puzzle])  # puzzle queue선언


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while queue:
        puzzle = queue.popleft()
        cnt = visited_dict[puzzle]
        z = puzzle.index('0') # 0(빈칸)의 위치
        
        if puzzle == '123456780': # 정답이라면
            return cnt  # 이동횟수를 리턴
        
        x,y = z//3,  z%3 # 2차원 배열의 행,렬
        
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2 and 0 <= ny <= 2: # 이동 가능한 위치일 경우
                nz = nx * 3 + ny                 # nx, ny(행,렬)을 리스트의 인덱스로 change
                puzzle_list = list(puzzle) # 문자열 -> list
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]
                new_puzzle = "".join(puzzle_list) # 딕셔너리를 위해 다시 문자열로
                
                # 방문하지 않았다면
                if visited_dict.get(new_puzzle, 0) == 0:
                    visited_dict[new_puzzle] = cnt 
                    queue.append(new_puzzle)
                    
    return -1
                    
# print(bfs())
        
print(visited_dict)
