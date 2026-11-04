# task 1
# def too(n):
#     if n == 0:
#         print("teg")
#     else:
#         if n > 0:
#             a = "eyreg"
#         else:
#             a = "sorog"

#         if n % 2 == 0:
#             b = "tegsh"
#         else:
#             b = "sondgoi"
#         print(a, b)
# n = int(input())
# too(n)

# task 2

# def unelgee(n):
#     if n < 0 or n > 100:
#         print("buruu onoo")
#     elif n >= 90:
#         print("A")
#     elif n >= 80:
#         print("B")
#     elif n >= 70:
#         print("C")
#     elif n >= 60:
#         print("D")
#     else:
#         print("F")

# n = int(input())
# unelgee(n)

# task 3

# def on(n):
#     if (n % 2 == 0 and n % 100 != 0)or n % 400 == 0:
#         print("ondor jil")
#     else:
#         print("engiin jil")
# n = int(input())
# on(n)

# task 4

# def gurvaljin(a, b, c):
#     if a + b <= c or a + c <= b or b + c <= a:
#         print("gurvaljin bish")
#     elif a == b == c:
#         print("tegsh talt")
#     elif a == b or a == c or b == c:
#         print("adil hajuud")
#     else:
#         print("engiin")

# a = int(input())
# b = int(input())
# c = int(input())

# gurvaljin(a, b, c)

# task 5

# def taxi(a, b):
#     if a <= 2:
#         tulbur = 3000
#     else:
#         tulbur = 3000 + (a - 2) * 1500

#     if b >= 22 or b < 6:
#         tulbur += 2000

#     print(tulbur)

# a = int(input())
# b = int(input())

# taxi(a, b)

# task 6

# def tegsh(n):
#     a = 0
#     for i in range(n+1):
#         if i % 2 == 0:
#             a += i
#     print(a)
# n = int(input())
# tegsh(n)    

# task 7

# def niilberts(n):
#     niilber = 0
#     while n > 0:
#         niilber += n % 10
#         n //= 10
#     print(niilber)

# n = int(input())
# niilberts(n)

# task 8

# def urvuulah(n):
#     urvuu = 0
#     while n > 0:
#         tsifr = n % 10
#         urvuu = urvuu * 10 + tsifr
#         n //= 10
#     print(urvuu)

# n = int(input())
# urvuulah(n)

# task 9

# def fiz_bazz(n):
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             print("pizbazz", end=" ")
#         elif i % 3 == 0:
#             print("piz", end=" ")
#         elif i % 5 == 0:
#             print("bazz", end=" ")
#         else:
#             print(i, end=" ")

# n = int(input())
# fiz_bazz(n)

# task 10

# def too():
#     nuuts = 37
#     oroldlogo = 0
#     while oroldlogo < 5:
#         taamag = int(input())
#         oroldlogo += 1
    
#         if taamag == nuuts:
#             print(f"taalaa {oroldlogo} oroldlogoor")
#         elif taamag <= 50:
#             print("baga bn")
#         else:
#             print("ih bn")
#     print("taasanguu")
# too()

# task 11

# def urjuuleh_husnegt(n):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(i * j, end=" ")
#         print()

# task 12

# n = int(input())
# urjuuleh_husnegt(n)

# n = int(input("too oruul guraljin hiigeed ogii :"))
# for i in range(1 , n+1):
#     for j in range(1 , n -1):
#         print("*", end= "")
#     for j in range(i-1):
#         print("*",end= "")
#     print()

# task13

# def find_pairs(arr, target):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 pairs.append((arr[i], arr[j]))
#     return pairs
# print(find_pairs([2, 7, 4, 5, 1], 6))
# print(find_pairs([1, 2, 3], 10))

# task 14

# arr = list(map(int, input().split()))
# best = arr[0]
# max_count = 0
# for x in arr:
#     if x not in set(arr[:arr.index(x)]):
#         count = arr.count(x)
#         if count > max_count:
#             best, max_count = x, count
# print((best, max_count))

# task 15
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rows = []
# cols = []
# for i in range(len(matrix)):
#     rows.append(sum(matrix[i]))

# for j in range(len(matrix[0])):
#     total = 0
#     for i in range(len(matrix)):
#         total += matrix[i][j]
#     cols.append(total)
# print((rows, cols))
# task 16
# def remove_duplicates(arr):
#     n = []
#     for i in arr:
#         if i not in n:
#             n.append(i)
#     return n
# a = list(map(int, input().split()))
# print(remove_duplicates(a))

# task 17
# def word_count(text):
#     words = text.split()
#     count = {}
#     for word in words:
#         count[word] = count.get(word, 0) +1
#     return count
# a = input()
# print(word_count(a))

# task 18
# def averages(grades):
#     avg = {}
#     for name,score in grades.items():
#         avg[name] = sum(score) / len(score)
#         max_score = max(avg.values())
#         best_students = "" 
#         for name , score in avg.items():
#             if score == max_score:
#                 best_students = name
#                 break
#     return avg, best_students
# a=  {"Анар": [80, 90, 70], "Болд": [60, 75, 90], "Сараа": [95, 85, 90]}
# print(averages(a))

# task 19
# python = {"Anar", "Bold", "Saraa", "Dorj"}
# math = {"Bold", "Gerel", "Dorj"}
# both = python & math
# a_pyton = python - math
# b_math = math - python
# total = len(python | math)
# print(f"hoyulandan; {both}")
# print(f"zowhon pyhton ywdag: {a_pyton}")
# print(f"zowhon math yawdag suragch: {b_math}")
# print(f"Niit: {total}")

# task 20
# def fathest_point(points):
#     max_dist = -1
#     best_point = None
#     for point in points:
#         x, y = point
#         dista = x**2 + y**2
#         if dista > max_dist:
#             max_dist = dista
#             best_point = point
#     return best_point, max_dist
# a=  [(1, 2), (3, 4), (-1, 5), (0, 0)]
# print(fathest_point(a))

# task 21
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) +1):
#         if n % i == 0:
#             return False
#     return True
# def primes_up_to(n):
#     prime_list = []
#     for i in range(2, n +1):
#         if is_prime(i):
#             prime_list.append(i)
#     return prime_list
# n = int(input())
# print(primes_up_to(n))

# task 22
# def find_all(arr, x):
#     count = []
#     for i in range(len(arr)):
#         if arr[i] == x:
#             count.append(i)
#     return count
# l= list(map(int, input().split()))
# n = int(input())
# print(find_all(l,n))

# task 23
# def find_phone(book,name):
#     for i in book:
#         current_name, phone_number = i
#         if current_name == name:
#             return phone_number
#     return "Oldosngue"
# book = [("Анар", "99112233"), ("Болд", "88001122"), ("Сараа", "95553344")]
# n = input()
# print(find_phone(book, n))

# task 24
# def bs_steps(arr,x):
#     left = 0
#     right = len(arr) -1
#     count = 0
#     while left <= right:
#         count += 1
#         mid = (right + left) // 2
#         if arr[mid] == x:
#             return mid, count
#         elif arr[mid] < x:
#             left = mid +1
#         else:
#             right = mid -1
#     return -1, count
# arr = list(map(int, input().split()))
# n = int(input())
# print(bs_steps(arr,n))
            
#  task 25
# def search_insert(arr, x):
#     left = 0
#     right = len(arr) -1
#     while left <= right:
#         mid  = (left + right) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid -1
#     return left
# n = list(map(int, input().split()))
# x = int(input())
# print(search_insert(n,x))

# task 26
# def bubble_sort(arr):
#     n = len(arr)
#     swap = 0
#     for i in range(n -1):
#         swapped = False
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1] , arr[j]
#                 swap +=1
#                 swapped = True
#         if not swapped:
#             break
#     return arr, swap
# arr = list(map(int, input().split()))
# print(bubble_sort(arr))

# task 27
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         min_idx  = i
#         for j in range(i+1, n):
#             if arr[j] <= arr[min_idx]:
#                 min_idx = j
#                 arr[i], arr[min_idx] = arr[min_idx] , arr[i]
#         print(f"{i+1}-r alham: {arr}")
#     return arr
# a = list(map(int, input().split()))
# print(selection_sort(a))

# task 28
# def merg_sort(arr):
#     if len(arr) <=1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = sort_unique(left)
#     right = sort_unique(right)
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
# def sort_unique(arr):
#     if not arr:
#         return []
#     sorted_arr = merg_sort(arr)
#     unique_arr = [sorted_arr[0]]
#     for x in sorted_arr[1:]:
#         if x != unique_arr[-1]:
#             unique_arr.append(x)
#     return unique_arr
# arr = list(map(int, input().split()))
# print(sort_unique(arr))

# task 29
# def top_three(scores):
#     tuple = []
#     for name, score in scores.items():
#         tuple.append((score, name))
#     tuple.sort(reverse=True)
#     result = []
#     for i in range(3):
#         result.append(tuple[i][1])
#     return result
# scores = {"Анар": 85, "Болд": 92, "Сараа": 78, "Дорж": 88, "Гэрэл": 95}
# print(top_three(scores))

# task 30
# n = int(input())
# scores = []
# for _ in range(n):
#     scores.append(int(input()))
# a = sorted(scores)
# max_score = max(scores)
# min_score = min(scores)
# avg_score = sum(scores) / n
# avg_count = 0
# for score in scores:
#     if score > avg_score:
#         avg_count += 1
# print(f"Erembelse: {a}")
# print(f"hamgiin ih: {max_score}")
# print(f"hamgiin baga: {min_score}")
# print(f"dundaj onoo: {avg_score}")
# print(f"dundajaas deesh onoo: {avg_count}")





