N, x= map(int, input().split())
array =list(map(int, input().split()))

def binary_search(array ,target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] < target:
            
         