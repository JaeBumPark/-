# A, B = [], []

N,M = map(int, input().split())

X= [list(map(int, input().split())) for _ in range(N)]
Y= [list(map(int, input().split())) for _ in range(N)]

# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)

# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)

for row in range(N):
    for column in range(M):
        print(X[row][column]+Y[row][column],end =' ')
    print()    