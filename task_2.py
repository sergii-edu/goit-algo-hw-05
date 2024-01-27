def binary_search_upper(arr, value):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    upper_value = arr[left] if left < len(arr) else None

    return (iterations, upper_value)


# Тестуємо пошук з верхньою межею

arr = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2]

print(binary_search_upper(arr, 0.8))  # (1, 0.8)

print(binary_search_upper(arr, 1.15))  # (3, 1.2)

print(binary_search_upper(arr, 1.25))  # (4, None)
