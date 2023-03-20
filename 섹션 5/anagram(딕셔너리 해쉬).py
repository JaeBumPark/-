import sys
# sys.stdin=open("input5.txt", "rt")
n=input()
m=input()

str1=dict()
str2=dict()

for i in n:
    str1[i] = str1.get(i, 0)+1 # get 으로 n의 알파벳 하나마다 value값 추가

for i in m:
    str2[i] = str2.get(i, 0)+1 # get 으로 m의 알파벳 하나마다 value값 추가
# print(str1["A"]) #왜 이러면 a의 갯수(value일까..?)
# print(str1.keys())
# print(str1.values())
# print(str1)
for i in str1.keys(): #str1에 있는 key들..
    if i in str2.keys():
       if str1[i]!=str2[i]: 
         print("no")
         exit() 
    else:
         print("no")
         exit() 
else:
      print("yes")                
     

# for i in str1.keys():
#     print(str1[i])
    

#keys()    