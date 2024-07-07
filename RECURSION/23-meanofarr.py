def meanofarr(arr,n):
    if n==0:
        return 0
    if n==1:
        return arr[0]
    return (arr[0] + (n-1)*meanofarr(arr[1:],n-1))/n
arr=[1,2,3,4,5,6]
n = len(arr)
print(meanofarr(arr,n))
