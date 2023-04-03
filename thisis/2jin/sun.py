def sequential_search(n, target, array):

  for i in range(n):

    if array[i]== target:
      return i +1


print("생성할원소개수를입력한다음한칸띄고찾을문자열을입력하세요.") 
inputdata = input().split()
n= int(inputdata[0])#원소의개수
target= inputdata[1]#찾고자하는문자열
print("앞서적은원소개수만큼문자열을입력하세요. 구분은띄어쓰기한칸으로합니다.") 
array= input().split()
# 순차탐색수행결과출력
print(sequential_search(n, target, array))