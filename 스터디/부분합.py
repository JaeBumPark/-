##백준 1806

import sys

n, m = map(int, sys.stdin.readline().split())  # n은 배열의 길이, m은 목표 부분합
arr = list(map(int, sys.stdin.readline().split()))  # 배열 입력받기

end = 0
intervalSum = arr[0]  # 첫 번째 원소로 초기화
ans = 99999

for start in range(n):  # start 포인터 이동
    # end 포인터를 이동하면서 부분합을 증가시킴
    while intervalSum < m and end < n - 1:
        end += 1
        if end == n:
             break 
        intervalSum += arr[end]

    # 부분합이 m 이상인 경우 길이 갱신
    if intervalSum >= m:
        ans = min(ans, end - start + 1)
    
    # start가 이동하므로 해당 값을 부분합에서 제거
    intervalSum -= arr[start]

# 조건에 맞는 부분합이 없을 경우 0을 출력, 그렇지 않으면 최소 길이 출력
if ans == 99999:
    print(0)
else:
    print(ans)
