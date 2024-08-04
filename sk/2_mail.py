def solution(n, m, send, errorlog):
    answer = []
    server_time = 0

    for time in send:
        # 서버로 메일 도착 시간 계산
        arrival_time_to_server = n + time

        # 서버에서의 메일 작업 시간 계산
        server_work_time = arrival_time_to_server + m

       
        # 서버 도착, 작업, 최종 도착 시간 리스트에 추가
        arrival_times = list(range(time, arrival_time_to_server + 1))
        work_times = list(range(arrival_time_to_server, server_work_time))

        # 서버 작업 중 장애 정보 확인
        for error_type, error_time in errorlog:
            if error_type == 1 and error_time in work_times:
                answer.append(-1)
                break
            elif error_type == 2 and error_time in work_times:
                 server_work_time = (max(work_times)+((max(work_times)-error_time)*2)) 
                 print("중간 :", server_work_time)
         # 메일의 최종 도착 시간 계산
        final_arrival_time = server_work_time + n
        final_arrival_times = list(range(server_work_time, final_arrival_time + 1))

        # # 정상적인 경우, 메일의 최종 도착 시간을 결과에 추가
        # if arrival_time_to_server not in answer:
        answer.append(final_arrival_time)

    return answer

# 예제 실행
n = 3
m = 5
send = [1, 2, 7, 8, 10, 11]
errorlog = [[1, 10], [2, 13], [1, 20]]
result = solution(n, m, send, errorlog)
print(result)  # [12, 13, -1, 18, 19, 22]

