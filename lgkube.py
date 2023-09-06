def rotate_2x2(matrix, row, col):
    # 2x2 행렬 시계 방향 회전 함수
    temp = matrix[row][col]
    matrix[row][col] = matrix[row+1][col]
    matrix[row+1][col] = matrix[row+1][col+1]
    matrix[row+1][col+1] = matrix[row][col+1]
    matrix[row][col+1] = temp

def count_transformations(matrix):
    # 행렬 A와 B의 크기 확인
    rows_a, cols_a = len(matrix), len(matrix[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    # 행렬 A를 행렬 B로 변환하는데 필요한 연산 횟수 계산
    transformations = 0
    while matrix != matrix_b:
        for i in range(rows_a - 1):
            for j in range(cols_a - 1):
                if matrix[i][j] != matrix_b[i][j]:
                    rotate_2x2(matrix, i, j)
                    print("fdf:", matrix)
                    transformations += 1

    return transformations

# 입력 예시
matrix_a = [
    [2, 5, 3],
    [1, 6, 9],
    [7, 4, 8]
]

matrix_b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = count_transformations(matrix_a)
print("행렬 A를 행렬 B로 바꾸는데 필요한 연산의 최솟값:", result)