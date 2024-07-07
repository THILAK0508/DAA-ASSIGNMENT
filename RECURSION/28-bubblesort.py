def bubble_sort_recursive(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    bubble_sort_recursive(arr, n - 1)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    bubble_sort_recursive(arr, len(arr))
    print("Sorted array:", arr)
