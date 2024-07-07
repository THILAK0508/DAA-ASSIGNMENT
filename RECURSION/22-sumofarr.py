def sumofarr(arr):
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return arr[0]
    return arr[0] + sumofarr(arr[1:])
arr=[1,3,6,76,3,2,54,4]
print(sumofarr(arr))
