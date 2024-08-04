def can_take_class(mandatory, elective):
    answer = 0
    elective.sort(key=lambda x: x[4])  # 선택 강의를 강의 평가 순위를 기준으로 정렬
    
    for e in elective:
        e_day, e_start, e_duration, e_building, e_rank = e
        conflict = False  # 선택 강의와 필수 강의의 시간이 겹치는지 여부를 나타내는 변수
        
        for m in mandatory:
            m_day, m_start, m_duration, m_building = m
            
            # 1번 조건: 선택 강의와 필수 강의 시간이 겹치면 안됨
            if e_day == m_day and e_building == m_building:
                if (e_start >= m_start and e_start < m_start + m_duration) or \
                   (m_start >= e_start and m_start < e_start + e_duration):
                    conflict = True
                    break
        
        # 2번 조건: 선택 강의는 필수 강의 시간이 붙어있으면 안됨 (단, 건물이 같은 경우에는 가능)
        if not conflict:
            for m in mandatory:
                m_day, m_start, m_duration, m_building = m
                if e_day == m_day and abs(e_start + e_duration - m_start) <= 1 and e_building != m_building:
                    conflict = True
                    break
        
        # 3번 조건: 필수 강의가 연리는 요일의 강의만을 수강할 수 있음
        if not conflict and e_day not in [m[0] for m in mandatory]:
            conflict = True
        
        # 4번 조건: 강의 평가 순위가 가장 낮은(강의 평가 순위값이 가장 작은) 강의를 신청
        if not conflict:
            answer += 1

    # 수강할 수 있는 강의가 없으면 -1을 반환
    if answer == 0:
        return -1

    return answer

# 테스트 케이스
mandatory = [[4, 13, 4, 1], [1, 14, 3, 1], [7, 13, 3, 2]]
elective = [[3, 13, 3, 4, 3], [4, 15, 2, 3, 2], [7, 16, 2, 3, 1], [7, 16, 3, 2, 4]]
result = can_take_class(mandatory, elective)
print(result)  # 결과 출력
