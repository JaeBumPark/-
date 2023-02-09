n=int(input())
l= [list(map(int, input().split())) for _ in range (5)]
l.insert(0, [0]*n) # 첫행에 0 박기
l.append([0]*n)

for x in l:
    x.insert(0,0)
    x.append(0)

# for x in l:
#     print(x, "봉우리 완성성")   
    
for i in range( )     