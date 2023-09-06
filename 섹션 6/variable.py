# 지역 변수와 전역 변수

def DFS1():
  cnt = 3   # 지역변수, 전역 변수중 지역이 우선!!, 이건 지역 변수
  print(cnt)
  
def DFS2():
  global cnt
  if cnt == 5:  
       cnt = cnt + 1  # 지역 변수가 생성 # global을 붙인다면 전역변수로 확인됨!
       print(cnt)
    
cnt = 5
DFS1()
DFS2()
print(cnt)      

     