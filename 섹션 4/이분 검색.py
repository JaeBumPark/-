n ,m = map(int,input().split()) # n은 array의 요소 갯수, m은 찾는 target 
array = [23, 86, 453, 43, 27]

array.sort()
lt =0. # 처음 index
rt = n-1 # 나중 index

while lt <=rt : ##lt가 rt보다 "작을"때까지 반복 ( 크면 탈출!)
      mid = int((lt+rt)//2)

      if array[mid] == m :
         print(mid)
         break

      elif array[mid] > m:
         
           rt = mid -1
      else:
           lt = mid + 1

         

