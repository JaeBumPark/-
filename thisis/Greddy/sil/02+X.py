n = list(map(int, input()))

length= len(n)
# print(n[2])
# print(type(n))

result = n[0]
for i in range (1, length):
 
    if n[i]<=1 or result<=1: # 다음것이 0이거나 첫번째가 0이면 
       result += n[i]

    else:
       result *= n[i] 

print(result)      
# data = input()

# result = int(data[0])

# print(result)