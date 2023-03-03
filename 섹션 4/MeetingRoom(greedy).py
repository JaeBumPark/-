n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))  # 튜플 형태로 들어감!
meeting.sort(key=lambda x: (x[1], x[0]))  # list에 들어간 tuple값에 기준을 세워 정렬하는 Lamda 함수, x[1]은 e(끝나는 시간), 두 번째 기준은 시작하는 값을 기준으로 오름차순 정렬
print(meeting)
et = 0  # 끝나는 시간
cnt = 0  # 답
for s, e in meeting:
    if s >= et: #첨에 et는 0이니까 무직권 들어감
        et = e
        cnt += 1

print(cnt)

