
msg = "It is Time" # 문자열
U=msg.upper() # 대문자 
l=msg.lower() # 

# print(U, "대문자로 변경")
# print(l, "소문자로 변경")
# print(msg.find('T')) #
# print(msg.count('T')) # T의 갯수


######
# print(msg[:2], "0부터 1까지")
# print(msg[3:5], "3에서 4까지")

# ######
# for x in msg:
#     if x.isupper(): # 만약 x가 대문자라면?
#        print(x, end=' ') #옆으로 출력    
       
##ASCII code

tmp = 'AZ'
for x in tmp:
    print(ord(x))       
    
tmp2= 'az'    
for y in tmp2:
    print(ord(y))
    
tmp3=90
print(chr(tmp3))    