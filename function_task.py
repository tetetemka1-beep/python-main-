# task 1
# def say_hello():
#     print("sainu")

# say_hello()
# task2
# def greet(name):
#     print("sainu",name)
# greet("bat")
# task3
# def introduce(name,age):
#     print(f"{name} n {age} nastai")
# introduce("Bat", 18)
# task4
# def add(a,b):
#     print(a+b)
# add(10,20)
# task5
# def result(nums):
#     return nums ** 2
# print(result(5))
# task 6
# def max_num(a,b):
#     return max(a,b)
# print(max_num(10,20))
# task 7
# def even_num():
#     num = int(input())
#     if num % 2 ==0:
#         return "even"
#     else:
#         return "odd"
# print(even_num())
# task 8
# def age_check():
#     age = int(input())
#     if age >= 18:
#         return "adult"
#     else:
#         return "minor"
# print(age_check())
# task 9
# def get_grade():
#     grade = int(input())
#     if 90 <= grade <= 100:
#         return "A"
#     elif 80 <= grade <= 89:
#         return "B"
#     elif 70 <= grade <= 79:
#         return "C"
#     elif 60 <= grade <= 69:
#         return "D"
#     elif 0 <= grade <= 59:
#         return "F"
#     else:
#         return "tiim muu ymu"
# print(get_grade())
# task 10
# def print_numbers(n):
#     for i in range(1,n+1):
#         print(i,end=" ")
# n = int(input())
# print_numbers(n)
# task 11
# def sum_num(n):
#     too = 0 
#     for i in range(1,n+1):
#         too += i
#     print(too)
# n = int(input())
# sum_num(n)
# task 12
# def count_even(n):
#     too = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             too +=1
#     print(too, end=" ")
# n = int(input())
# count_even(n)
# task 13
# def count_dight(nums):
#     len(nums)
#     print(nums)
# nums = int(input())
# count_dight(nums)
# task 14
# def find_max(nums):
#     max_num = nums[0]
#     for i in range(len(nums)):
#         if nums[i] > max_num:
#             max_num = nums[i]
#     return max_num
# nums = [4, 8, 2, 15, 6]
# print(find_max(nums))
# task 15
# def find_min(nums):
#     min_num = nums[0]
#     for i in range(len(nums)):
#         if nums[i] < min_num:
#             min_num = nums[i]
#     return min_num
# nums = [7, 3, 9, 1, 5]
# print(find_min(nums))
# task 16
# def count_even(nums):
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] % 2 == 0:
#             count += 1
#     return count
# nums = [1, 2, 4, 7, 8, 10]
# print(count_even(nums))
# task 17
# def list_sum(nums):
#     total = 0
#     for i in range(len(nums)):
#         total += nums[i]
#     return total
# nums = [10, 20, 30, 40]
# print(list_sum(nums))
# task 18
# def get_age(students, name):
#     return students[name]
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# print(get_age(students, "Sara"))
# task 19
# def find_student(students, name):
#     if name in students:
#         return "Found"
#     else:
#         return "Not found"
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# print(find_student(students, "Sara"))
# task 20
# def average_score(students):
#     total = 0
#     count = 0
#     for name in students:
#         total += students[name]
#         count += 1
#     return total / count
# students = {
#     "Bat": 80,
#     "Sara": 90,
#     "Bold": 70
# }
# print(average_score(students))
# task 21
# def unique_numbers(nums):
#     return set(nums)
# nums = [1, 2, 2, 3, 3, 4]
# print(unique_numbers(nums))
# task 22
# def unique_numbers(nums):
#     return set(nums)
# nums = [1, 2, 2, 3, 3, 4]
# print(unique_numbers(nums))
# task 23
# def greet(name="Guest"):
#     print("Hello", name)
# greet()
# greet("Bat")
# task24
# def power(num, exponent=2):
#     return num ** exponent

# print(power(5))
# print(power(2, 3))
# # task25
# def discount(price, percent=10):
#     result = price - price * percent / 100
#     return result

# print(discount(10000))
# print(discount(10000, 20))
# # task26
# def sum_all(*args):
#     total = 0

#     for i in args:
#         total += i

#     return total

# print(sum_all(1, 2, 3))
# print(sum_all(10, 20, 30, 40))
# # task27
# def find_max(*args):
#     max_num = args[0]

#     for i in args:
#         if i > max_num:
#             max_num = i

#     return max_num

# print(find_max(5, 8, 2, 10, 3))
# # task28
# def count_even(*args):
#     count = 0

#     for i in args:
#         if i % 2 == 0:
#             count += 1

#     return count

# print(count_even(1, 2, 4, 7, 8, 10))
# # task29
# def show_info(**kwargs):
#     for key in kwargs:
#         print(key + ":", kwargs[key])

# show_info(name="Bat", age=18, city="Ulaanbaatar")
# # task30
# def calculate_total(**prices):
#     total = 0

#     for name in prices:
#         total += prices[name]

#     return total

# print(calculate_total(
#     apple=2000,
#     banana=3000,
#     orange=2500
# ))