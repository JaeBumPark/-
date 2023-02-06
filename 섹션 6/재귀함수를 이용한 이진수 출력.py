
def DFS(x):
    if x==0:
        return
    else:
        print(x%2, end='')
        DFS(x//2)
        
if __name__=="__main__":
   n=int(input())
   DFS(n)