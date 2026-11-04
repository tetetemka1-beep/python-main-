# quick sort

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [8, 3, 1, 7, 0, 10, 2]
# print(quick_sort(numbers))

# task 2

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [5, 2, 9, 1, 7]
# print(quick_sort(numbers))

# task 3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [4, 2, 4, 1, 2, 3, 1]
# print(quick_sort(numbers))

# task 4

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [3, -5, 0, 8, -2, 1]
# print(quick_sort(numbers))

# task 5

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [9, 2, 7, 1, 5, 3]
# print(quick_sort(numbers))
# print(quick_sort(numbers)[:3])

# task 6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [9, 2, 7, 1, 5, 3]
# print(quick_sort(numbers))
# print(quick_sort(numbers)[-2:])

# task 7
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num[1] < pivot[1]:
#             left.append(num)
#         elif num[1] == pivot[1]:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [("Bat", 85), ("Bold", 70), ("Saraa", 95), ("Anu", 60)]
# print(quick_sort(numbers))

# task 8

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if len(num) < len(pivot):
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = ["banana", "cat", "apple", "hi", "dog"]
# print(quick_sort(numbers))

# task 9
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#             n = len(arr)
#             if n % 2 == 1:
#                 return arr[n // 2]
#             else:
#                 return (arr[n // 2 - 1] + arr[n // 2]) / 2
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers))

# task 10

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# a = [8, 3, 5]
# b = [2, 9, 1]
# print(quick_sort(a+b))
