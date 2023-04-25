N, M = map(int, input().split())

K= list(map(int, input().split()))

#1부터 10까지 공의 무게를 담을 list// index 번호는 무게, index에 해당하는 값은 공이 몇개가 있는지
array=[0] * 11

for i in K: #공 중에서   
    array[i] += 1  #각 무게별 공의 개수

# print(array)    
result = 0
for j in range(1, M+1): #1부터 M무게 까지
    if j  