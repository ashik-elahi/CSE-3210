def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return True

    return False


arr = [2, 3, 4, 5, 10, 40]
x = 4

result = binary_search(arr, x)

print(result)
