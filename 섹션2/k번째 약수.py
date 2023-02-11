
n, k =map(int, input().split())
cnt=0
for i in range(1, n+1): #개쩐다 index = 합으로 ㄷ ㄷ
    if n%i ==0:
      cnt+=1
    if cnt ==k:
       print(i)
       break;
