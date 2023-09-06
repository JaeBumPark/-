import sys
def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
       return False
    if M[x][y] == 1:  #1이면
       cnt.append(1)
       M[x][y] = 0
       dfs(x-1,y)
       dfs(x,y-1)
       dfs(x+1,y)
       dfs(x,y+1)
       return True
    return False  


N = int(sys.stdin.readline())

M = [list(map(int, sys.stdin.readline().split())) for _ in range (N)]

cnt= []
result_list=[]
result = 0
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
           result += 1
           result_list.append(len(cnt))
           cnt = []
             
print(result) 
result_list.sort()     
for i in result_list:
    print(i) 