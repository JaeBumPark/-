##search case
import sys

N = int(sys.stdin.readline())

farm = [list(map(int, sys.stdin.readline().split())) for _ in range (N)] # 농장 
total = 0
s=e= (N//2)
for i in range(N):
    for j in range(s,e+1):
        total += farm[i][j]
    
    if i < (N//2):
       s -= 1
       e += 1
       
    else :
       s += 1
       e -= 1
       
print(total) 

# N = 5
# M = 2
# if M==N//2:
#    print("yes")
# else:
#    print("no")     