def DFS(l, sum) # l은 index 번호, sum은 부분집합의 합 
if sum >= c:
   print(sum)
else:
   DFS(l+1)

if __name__=="__main__":
  c, n = map(int, input().split())
  a=[0]*n
  result=-2412341234123
  for i in range(n):
    a[i]=int(input())
    
  DFS(0,0)    

    
    