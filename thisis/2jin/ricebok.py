N,M = map(int, input().split())

D = list(map(int, input().split()))

start=0
end=max(D)
result = 0

while start <= end:
      total=0 # 잘린 떡의 길이
      mid = (start+end)//2
      for x in D:
          if x > mid: # mid 보다 떡의 길이가 길다면
             total += x-mid
          
      if total < M: # 잘린 떡이 필요한 떡의 길이보다 작다면,
             end = mid -1
      else:
            result = mid
            start = mid + 1
print(result)                       
                     
                     