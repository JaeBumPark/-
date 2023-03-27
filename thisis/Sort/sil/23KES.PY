n=int(input())
S_list=[]
for i in range(n):
    [name, korean, eng, math] = map(str, input().split()) # 각 요소만큼 값을 input()

    S_list.append([name, int(korean), int(eng), int(math)])

sorted_list=sorted(S_list, key=lambda x: (-x[1], x[2], -x[3], x[0])) # 국어 성적이 감소하는 순, 영어 성적이 증가하는 순, 수학 점수가 감소하는 순, 이름 사전순

for j in sorted_list:
    print(j[0])
