## 1. k(한번에 건너 뛸 수 있는 돌의 갯수)가 연속되는 0의 갯수보다 작다면, 불가능
## 2. 크기가 넘 커서, 완탐은 불가능
## 3.

def solution(stones, k):
    answer = 0
    left = 1
    right= max(stones)
    cnt = 0  # 최소 인원(left)은 1명, 최대 인원(right)은 stones 배열에서 가장 큰 값으로 설정
    # ct는 현재 중간값(mid)에서 건널 수 없는 돌의 연속된 횟수
    
    while left <= right:  # 이분 탐색을 진행 (탐색 범위가 남아 있는 동안 반복)
        cnt = 0  # 연속된 무너진 돌의 개수를 카운트하기 위한 변수 초기화
        mid = (left + right) // 2  # 중간값(mid) 설정. 현재 이 인원(mid)이 건널 수 있는지를 검사
        
        for stone in stones:
            if stone - mid <= 0:  # 돌이 버틸 수 없는 경우 (돌의 값이 중간값보다 작거나 같을 때)
                cnt += 1  # 연속된 무너진 돌 개수를 증가시킴
            else:
                cnt = 0  # 버틸 수 있는 돌을 만났으므로 연속된 0의 개수를 초기화
            
            if cnt >= k:  # 연속된 무너진 돌이 k개 이상(같거나 크면)
                break  
        
        if cnt < k:  # 연속된 무너진 돌이 k개 미만이면
            left = mid + 1  # 더 많은 인원을 탐색하기 위해 범위를 늘림 (mid 인원은 건널 수 있음)
            
        else:
            answer = mid  # 현재 mid 인원은 건널 수 없음. 일단 저장하고
            right = mid - 1  # 더 적은 인원을 탐색하기 위해 범위를 줄임
    
    return answer  # 최종적으로 가능한 최대 인원을 반환
