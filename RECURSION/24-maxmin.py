def find_max(arr, n):
    if n == 1:
        return arr[0]
    
    max_of_rest = find_max(arr, n - 1)

    return max(arr[n - 1], max_of_rest)

def find_min(arr, n):

    if n == 1:
        return arr[0]

    min_of_rest = find_min(arr, n - 1)

    return min(arr[n - 1], min_of_rest)

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)

max_value = find_max(arr, n)
min_value = find_min(arr, n)

print("Maximum value in the array: ",max_value)
print("Minimum value in the array: ",min_value)
