# merge sort

# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result
# numbers = [38, 27, 43, 3, 9, 82, 10]
# print(merge_sort(numbers))

# task 2
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [38, 27, 43, 3, 9, 82, 10]

# print(merge_sort(numbers))

# task 3
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result
# numbers = [5, 3, 8, 3, 1, 5, 5]
# print(merge_sort(numbers))

# task 4

# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result
# numbers = [3, -2, 0, -7, 5, -1]
# print(merge_sort(numbers))

# task 5

# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result
# numbers = [7, 2, 9, 4, 1, 6]
# a = (merge_sort(numbers))
# m = []
# b = []
# for i in a:
#     if i % 2 == 0:
#         m.append(i)
#     else:
#         b.append(i)
# print(m+b)

# task 6

# def merge_sort(c):
#     if len(c) <= 1:
#         return c
#     mid = len(c) // 2
#     left = c[:mid]
#     right = c[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# a = [1, 4, 7, 10]
# b = [2, 3, 8]
# c = a + b
# print(merge_sort(c))

# task 7
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# numbers = list(map(int, input().split()))

# print(merge_sort(numbers))
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# numbers = [8, 3, 5, 4, 7, 6, 1, 2]
# print(merge_sort(numbers))