#최솟갑 구하기!


arr = [ 7, 4, 6, 8, 13, 2, 6]
arrMin = float("inf") #최솟값 변수, 첨에 존나 큰 값을 넣음

for i in range(len(arr)): # arr의 크기 만큼 돈다리
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)        