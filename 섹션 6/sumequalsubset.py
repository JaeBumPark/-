def DFS(l, sum): #l은 tree의 level, sum은 부분집합!
    if l == n:
       if total == total-sum: # 두 부분집합의 합이 같으면!@!!!
          print("yes~~")
          exit(0) 
    else:
      DFS(l+1, sum+1)
      DFS(l+1, sum)       

if __name__=="__main__":
  
  n = int(input())
  a=list(map(int, input().split()))
  total=sum(a)
  DFS(0,0)