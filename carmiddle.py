from itertools import combinations

def count_combinations(arr, q, mi):
    count = 0

    for r in range(3, n + 1):
        for combo in combinations(arr, r):
            if sorted(combo)[1] == mi:
                count += 1

    return count

# 입력 받기
n, q = map(int, input().split())
mileages = list(map(int, input().split()))
mi_values = [int(input()) for _ in range(q)]

for mi in mi_values:
    result = count_combinations(mileages, q, mi)
    print(result)