score = [
    [4, 9, 8, 10, 10],
    [9, 2, 2, 5, 8],
    [5, 10, 5, 3, 4],
    [7, 9, 10, 5, 4],
    [4, 4, 10, 1, 4]
]

darts = [4, 9, 14, 19, 24, 12, 23]

def solutions(score, darts):
    answer = 0
    popped = set()  # 이미 터진 위치를 저장할 집합

    for dart in darts:
        x = (dart - 1) // 5  # 다트 번호를 행으로 변환
        y = (dart - 1) % 5   # 다트 번호를 열로 변환

        # 이미 풍선이 터진 위치라면 점수를 더하지 않음
        if (x, y) in popped:
            continue

        answer += score[x][y]  # 점수 더하기

        # 가로 줄, 세로 줄 풍선 5개를 모두 터트리면 10점 추가
        if sum(1 for i in range(5) if (x, i) in popped) == 4 or \
           sum(1 for i in range(5) if (i, y) in popped) == 4:
            answer += 10

        popped.add((x, y))  # 다트가 맞춘 위치를 추가
        print(popped)
    # 게임 시작 시 10점 차감 및 추가 다트에 대한 5점 차감
    answer -= 10 + 5 * (len(darts) - 5)

    return answer

result = solutions(score, darts)
print("결과:", result)