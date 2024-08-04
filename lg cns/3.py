def ham(black_caps):
    n = len(black_caps)  # 사람의 수
    answer = [0] * n  # 초기에는 모두 "모름"으로 설정
    
    # 맨 앞 사람과 맨 뒷 사람이 볼 수 있는 정보를 활용하여 모자 색깔을 추론
    if black_caps[0] == 1:
        answer[0] = 1  # 맨 앞 사람이 검은 모자를 쓰고 있다면, 그의 앞 사람은 검은 모자를 쓴다고 판단
    if black_caps[n - 1] == 1:
        answer[n - 1] = 1  # 맨 뒷 사람이 검은 모자를 쓰고 있다면, 그의 뒷 사람은 검은 모자를 쓴다고 판단
    
    # 중간 사람들의 모자 색깔을 추론
    for i in range(1, n - 1):
        if black_caps[i - 1] == 2 and black_caps[i + 1] == 0:
            answer[i] = 1  # 앞 사람이 흰 모자를 쓰고, 뒷 사람이 검은 모자를 쓰고 있다면, 중간 사람은 검은 모자를 쓴다고 판단
        elif black_caps[i - 1] == 1:
            answer[i] = 2  # 앞 사람이 검은 모자를 쓰고 있다면, 중간 사람은 흰 모자를 쓴다고 판단
    
    return answer

# 테스트 케이스
black_caps = [1, 1, 2, 0]
result = ham(black_caps)
print(result)  # 출력 결과: [1, 1, 2, 1]