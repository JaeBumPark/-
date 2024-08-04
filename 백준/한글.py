def korean_to_english_consonant(korean_consonant):
    # 한글 자음에 대한 딕셔너리 매핑
    korean_to_english = {
        'ㄱ': 'g', 'ㄲ': 'kk', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'tt',
        'ㄹ': 'r', 'ㅁ': 'm', 'ㅂ': 'b', 'ㅃ': 'pp', 'ㅅ': 's',
        'ㅆ': 'ss', 'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'ch',
        'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h'
    }
    # 영어 발음으로 변환하여 반환
    return korean_to_english.get(korean_consonant, korean_consonant)


name = "박재범"  # 사용자 입력 대신 고정된 값 사용
surname = name[0]  # 성 추출
english_surname = korean_to_english_consonant(surname)  # 성의 첫 번째 자음을 영어로 변환

print(english_surname)

# # 영어로 변환된 성의 첫 번째 자음을 이용하여 출력 형태 구성
# for i in range(7):
#     for j in range(7):
#         if (i in [0, 1, 3, 4] and j == 3) or (i == 2 and j in [1, 2, 3, 4, 5]):
#             print(english_surname, end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# for i in range(7):
#     for j in range(7):
#         if i == 5 and (j in [1, 2, 3, 4, 5, 6]):
#             print(english_surname, end=' ')
#         else:
#             print(' ', end=' ')
#     print()
