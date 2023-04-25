
n=int(input())
a=list(map(int,input().split()))
m=int(input())

a.sort()    #오름차순으로 sort

for _ in range(m):
    a[n-1] -= 1
    a[0] += 1
    a.sort()
    
print((a[n-1]-a[0]))    