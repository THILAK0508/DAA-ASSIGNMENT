def nnatural(n):
    if n ==1:
        return 1
    else :
        return n+nnatural(n-1)
n = 5
print(nnatural(n))