n = int(input())
meeting = []

for i in range(n):
    s, e =map(int, input().split())
    meeting.append((s,e))
    
meeting.sort(key=lambda x:(x[1],x[0]))    #끝나는 기준으로
       
# print(meeting)    
et=0 ## e를 저장할 변수
result = 0
for s,e in meeting:
    if et <= s:
       et = e 
       result += 1
       
print(result)        
    
