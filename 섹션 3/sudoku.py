l = [list(map(int, input().split())) for _ in range (9)]
print(l)
ch=[0]*10
# 중복이 없다..?
def check(v):
    for i in range (9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range (9): 
            ch1[v[i][j]]=1# 행 check
            ch2[v[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9: # sum 함수로 list의 핪
            return False   
        else:
            return True   
          
    for i in range(3):
        for j in range(3):
                ch3= [0]*10
                for s in range(3):
                    for k in range(3):
                        ch[v[i*3+s][j*3+k]] = 1 
        if sum(ch3)!= 9:
           return False 
        else:
           return True   
if check(l):
   print("yes")
else:
   print("No!!~!!!")                   