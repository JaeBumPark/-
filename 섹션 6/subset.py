def DFS(x):
    if x==n+1: # 종료지점
       for i in range(1, n+1):
           if ch[i] == 1:
                print(i, end = '') 
       print()         
                
         #print(x)
    else:
        ch[x]=1
        DFS(x+1)
        ch[x]=0 
        DFS(x+1)      
          
 #재귀 함수는 반복문의 대체제!!!
 
 
if __name__=="__main__": #main script
    n=int(input())
    ch=[0]*(n+1) # check 변수
    DFS(1)
      
         