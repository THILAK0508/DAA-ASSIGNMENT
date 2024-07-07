import math
def reverse(n,k):
    if n <10:
        return n
    digit = n %10  
    return digit*10**(k-1)+reverse(n//10,k-1)
n=1243
k=math.floor(math.log10(n))+1 # number of digits in n
print(reverse(n,k)) 
