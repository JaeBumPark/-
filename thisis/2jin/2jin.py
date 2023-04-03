###재귀 함수를 이용한 이진 탐색
def binary_search(array, target, start, end): # array는 배열, target은 찾는 순자, start,end는 index 
    if start > end:
       return False
    mid=(start+end)//2
    
    if array[mid] == target:
       return mid
    
    elif array[mid] > target:
         return binary_search(array, target, start, mid-1) # mid에서 1줄이고 재귀
         
    else:
         return binary_search(array, target, mid+1, end) # mid에서 1줄이고 재귀   
     
n, target = map(int, input().split())     
array = list(map(int, input().split()))

result =binary_search(array, target, 0, n-1)

if result==False:
   print("원소가 읎어요") 
else:
   print(result+1)    
   
###재귀 함수를 이용한 이진 탐색
def binary_search(array, target, start, end):
    while start < end:
       mid = (start+end)//2
       if array[mid] == target:
          return mid
       elif array[mid] > start:
            end = mid - 1
       else:
            start= mid + 1     
    return False         