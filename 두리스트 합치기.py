import sys
sys.stdin=open("input3.txt", "rt")
n=int(input())
k=list(map(int,input().split()))
print(k)
m=int(input())
l=list(map(int,input().split()))
pt1=0
pt2=0 #두 배열의 포인터들
c=[] #빈 리스트
while pt1<n and pt2<m: #while문을 사용하는 것을 기억하자.
    if k[pt1]<=l[pt2]: 
        c.append(k[pt1]) #배열에 append로 추가
        pt1+=1
    else:
        c.append(l[pt2])  
        pt2+=1 
if pt1<n: #남았을경우
   c= c+k[pt1: ]
if pt2<m:
   c= c+l[pt2: ]
print(c)    

       
       