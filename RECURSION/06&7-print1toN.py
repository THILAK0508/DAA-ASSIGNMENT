def print1toN(n):
    if n>0:
        print1toN(n-1)
        print(n)
def printNto1(n):
    if n>0:
        print(n)
        printNto1(n-1)
        
x=5
print(print1toN(x))
print(printNto1(x))