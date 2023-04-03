# def binary_search(array, target, start, end):
#     while start <= end:
#       mid = (start+end)//2
#       if array[mid] == target:
#          return mid
#       elif array[mid] > target:
#          end = mid -1
#       else:
#          start = mid + 1
#     return None

               
# N = int(input())
# array=list(map(int, input().split()))
# array.sort() # 이진 탐색을 위해 정렬
# M = int(input())
# array2=list(map(int, input().split()))

# for i in array2:
#     result=binary_search(array,i,0,N-1)
#     if result != None:
#        print("yes", '')
#     else:
#        print("no", '')     

N = int(input())
array=list(map(int, input().split()))

M = int(input())
array2=list(map(int, input().split()))

for i in array2:
    if i in array:
       print("yes", end='') 
    else:   
       print("no", end='') 
 