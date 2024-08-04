L = [list(map(str, input().split())) for _ in range(5)]
# length = 0 
# for x in L:
#     print(x) #2차원 리스트 중 각 list를 출력
for i in range(max(len(r) for r in L)):
    for j in range(5):
        print(L[i][j], end = '')
    
    