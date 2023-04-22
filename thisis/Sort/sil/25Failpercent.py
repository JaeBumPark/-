def solution(N, stages):
    
    answer = []
    length = len(stages)
    fail = 0
    for i in range(1, N+1): # N은 도전하고 있는 스테이지 갯수
        # 해당 스테이지 사람의 명 수 계산
        count = (stages.count(i))
        # 실패율 구하기    
        if length == 0:
           fail = 0
        else:
           fail = count / length
           
        answer.append((i, fail))     # 튜플 값으로 list에 append
        length -= count
        
     
    answer = sorted(answer, key=lambda x:x[1], reverse=True)   # 실패율 내림차순(높은순으로)으로 정렬
    
    answer = [j[0] for j in answer] ## answer중 [0]번째 요소 (stage 숫자)를 저장
    
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))