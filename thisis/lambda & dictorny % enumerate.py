##key=lambda

# list = []

# list.append(("Hong", 8))
# list.append(("AIM", 5))
# list.append(("LEE", 7))

# NAME_SORTED = sorted(list, key=lambda x:x[0])
# NUM_SORTED = sorted(list, key=lambda x:x[1])

# print(NAME_SORTED, "이름순 정렬")
# print(NUM_SORTED, "숫자 순 정렬")

## enumerate

team= ["KIM", "Hong", "LEE"]

for key, value in enumerate(team):
    print(key, value)