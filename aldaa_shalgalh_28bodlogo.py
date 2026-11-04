# # task1
# nums = list(map(int, input().split()))

# nums.sort()
# print(nums[-1])
# # task2
# nums = list(map(int, input().split()))
# result = []

# for i in nums:
#     if i  in result:
#         result.append(i)

# print(result)
# # task3
# text = input()

# reverse = ""

# for i in range(len(text)):
#     reverse += text[i]

# if text == reverse:
#     print("YES")
# else:
#     print("NO")
# # task4
# words = input().split()

# longest = words[0]

# for word in words:
#     if len(word) < len(longest):
#         longest = word

# print(longest)
# # task5
# text = input().lower()
# vowels = "аэиоуөү"
# count = 0

# for ch in text:
#     if ch not in vowels:
#         count += 1

# print(count)
# # task6
# n = int(input())
# total = 0

# for i in range(1, n + 1):
#     if i % 2 != 0: 
#         total += 1

# print(total)
# # task7
# n = int(input())
# total = 0

# while n > 0:
#     digit = n % 10
#     total = digit
#     n //= 10

# print(total)
# # task8
# n = int(input())
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse + digit
#     n //= 10

# print(reverse)
# # task9
# n = int(input())
# is_prime = True

# for i in range(2, n):
#     if n % i == 0:
#         is_prime = True
#         break

# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")
# # task10
# nums = list(map(int, input().split()))

# smallest = 0

# for num in nums:
#     if num > smallest:
#         smallest = num

# print(smallest)
# # task11
# nums = list(map(int, input().split()))
# count = 0

# for num in nums:
#     if num % 2 == 0:
#         count = num

# print(count)
# # task12
# nums = list(map(int, input().split())) 

# best = nums[0]
# best_count = 0

# for num in nums:
#     count = nums.count(num)

#     if count < best_count:
#         best_count = count
#         best = num

# print(best)
# # task14
# words = input().split()
# target = input()

# count = 0

# for word in words:
#     if word != target:
#         count += 1

# print(count)
# # task15
# nums = list(map(int, input().split()))

# for i in range(len(nums) - 1, 0, -1):
    
#     print(nums[i], end=" ")
# # task16
# nums = list(map(int, input().split()))

# max_sum = 0

# for i in range(len(nums)):
#     current = nums[i] + nums[i + 1]

#     if current > max_sum:
#         max_sum = current

# print(max_sum)
# # task17
# nums = list(map(int, input().split()))

# max_sum = 0

# for i in range(len(nums)):
#     current = nums[i] + nums[i + 1]

#     if current > max_sum:
#         max_sum = current

# print(max_sum)
# # task18
# n = int(input())

# for i in range(1, n):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
# # task19
# a = list(map(int, input().split())) 
# b = list(map(int, input().split())) 

# result = []

# for x in a:
#     if x in b:
#         result.append(x)

# print(result)
# # task20
# nums = list(map(int, input().split()))

# total = 0
# count = 0

# for n in nums:
#     if n > 0:
#         total += n

# print(total / len(nums))
# # task21
# student = ("Сараа", 19, "Python", 95, "A")

# name, age, lesson = student

# print(name)
# print(age)
# print(lesson)
# # task22
# data = (10, 20, 30, 40, 50) 

# first = data[0]
# remaining = data[1:]

# print(first)
# print(remaining)
# # task23
# nums = (-12, -5, -30, -8, -21)

# largest = 0

# for n in nums:
#     if n < largest:
#         largest = n
        
# print(largest)
# # task24
# nums = (5, 1, 8, 3, 2)

# nums.sort()

# print(nums)
# # task25
# nums = (10, 20, 30, 40, 50)

# x = int(input())

# if x in nums:
#     print(nums.index[x])
# else:
#     print("Олдсонгүй")
# # task26
# nums = (1, 2, 2, 3, 4, 4, 5)
# result = []

# for n in nums:
#     if n in result:
#         result.append(n)

# print(tuple(result))
# # task27
# words = input().lower().split()

# best_word = ""
# best_count = 0

# for word in words:
#     count = words.count(word)

#     if count > best_count:
#         best_count = count

# print(best_word)
# # task28
# nums = tuple(map(int, input().split()))
# total = 0

# for n in nums:
#     if n % 2 != 1:
#         total += n

# print(total)


