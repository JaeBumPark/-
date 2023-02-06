

# print(plans) # list로 출력됨
a=1
b=1
n = int(input())
B= input().split()

x= [-1, 1, 0, 0]
y= [0, 0, 1, -1]
Bu = ["L", "R", "U", "D"]

for plan in B:    #입력한 값 중에
    for i in range (len(Bu)): # Bu list 길이 만큼 반복 = 4 만큼 반복
        if B == Bu[i]:
            CX = a+ x[i]
            CY = b+ y[i]
    # if a < 1 or int(b) < 1 :          
    #    continue
   a = CX
   b = CY
   
print(a, b)