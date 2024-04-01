def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

def is_present(arr, x):
    lb = lower_bound(arr, x)
    return lb < len(arr) and arr[lb] == x

sorted_array = [1, 2, 3, 4, 4, 4, 5, 6, 7]
x = 4
print("Lower Bound:", lower_bound(sorted_array, x))
print("Upper Bound:", upper_bound(sorted_array, x))
print("Is Present:", is_present(sorted_array, x))