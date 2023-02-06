#DFS 전위 순회
def DFS(v):
    if v>7:
        return
    else:
        print(v, end= "") # 함수 본연의 일
        DFS(v*2) # 왼쪽 노드를 호출
        DFS(v*2+1)

if __name__=="__main__":
    DFS(1)
    
#DFS 중위 순회    
def DFS(v):
    if v>7:
        return
    else:
        DFS(v*2) # 왼쪽 노드를 호출
        print(v, end= "") # 함수 본연의 일
        DFS(v*2+1)

if __name__=="__main__":
    DFS(1)
    