
def DFS(x):
    if x>0:
         #print(x)
         DFS(x-1)
         print(x, end=" ") # why 역순 출력? stack을 활용하기 때문에? 
         
 #재귀 함수는 반복문의 대체제!!!
 
 
if __name__=="__main__": #main script
    n=int(input())
    DFS(n) #깊이 우선 탐색, 재귀함수 
      
         