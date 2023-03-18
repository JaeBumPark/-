def DFS1():
    print(cnt)
    # cnt가 1)지역 변수인지 먼저 check 하고 사용
    # 2) 없으면 전역변수로
def DFS2():
    cnt=6
    print(cnt)
        
if __name__=="__main__":    
   cnt =5     
   DFS1()
   DFS2()