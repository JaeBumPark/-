n,m =map(int, input().split())
Dab = 0
while n>1:
   if(n % m) == 0:
      n = n/m
      print(n, "나누기 한거")
      Dab += 1
   else:
      n -= 1  
      print(n, " 빼기한거")
      Dab += 1
print(Dab)     
    
    