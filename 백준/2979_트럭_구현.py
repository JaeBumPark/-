import sys

time=[0]*100
A,B,C=map(int,sys.stdin.readline().split())

cal1=0 
cal2=0
cal3=0 # 시간

for _ in range(3):
  start,end=map(int,input().split())
  for i in range(start, end):
      time[i] += 1

for j in time:
    if j == 3:
       cal3 += 1  
    if j == 2:
       cal2 += 1   
    if j == 1:
       cal1 += 1              
 
print(cal3*C*3+cal2*B*2+cal1*A*1)            
   

