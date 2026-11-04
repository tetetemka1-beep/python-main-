# task 1
# nums = [1, 2, 2, 3, 4, 4, 5]
# a = set(nums)
# print(a)
# 2
# fruits = {"apple", "banana"}
# fruits.update({"orange"})
# print(fruits)
# 3
# fruits = {"apple", "banana", "orange"}
# fruits.remove("banana")
# print(fruits)
# 4
# nums = {10, 20, 30, 40}
# if 20 in nums:
#     print("yes")
# else:
#     print("no")
# 5
# nums = {1,2,2,3,3}
# a = set(nums)
# print(len(a))
# 6
# names = ["Bat", "Sara", "Bat", "Bold", "Sara", "Anu"]
# a = set(names)
# print(len(a))
# 7
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a | b
# print(c)
# 8
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a & b
# print(c)
# 9
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a - b
# print(c)
# 10
# python_students = {"Bat", "Sara", "Bold", "Anu"}
# java_students = {"Sara", "Bold", "Temuulen"}
# c = python_students & java_students
# print(c)
# 11
# a = {"Bat", "Sara", "Bold", "Anu"}
# b = {"Sara", "Bold", "Temuulen"}
# c = a - b | b - a
# print(c ) 
# 12
# b = set("banana")
# print(len(b))
# 13
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
# }
# print(student)
# 14
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
# }
# print(student["name"])
# 15
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 85
# }
# student.update({"score": 95})
# print(student["score"])
# 16
# student = {
#     "name": "Anu",
#     "age": 18
# }
# student["city"] = "Ulaanbaatar"

# print(student)
# 17
# student = {
#     "name": "Bold",
#     "age": 20,
#     "score": 88
# }
###########################################
# a = list(map(int,input().split()))
# v = sorted(list(set(a)))[-2]
# print(v)

# a = list(map(int,input().split()))
# v = sorted(list(set(a)), reverse=True)[-2]
# print(v)

# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]
# best = 0
# cur = 0 
# for i in nums:
#     if i % 2 != 0:
#         cur += 1
#         best = max(best,cur)
#     else:
#         cur = 0   
# print(best)

# a = [1, 2, 4, 2, 3, 5, 7, 1]
# b = 1
# c = 1
# for i in range(len(a)):
#     if a[i]<a[i-1]:
#         c +=1
#         b = max(b,c)
#     else:
#         c = 0   
# print(b)

# m = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# print(m[0])

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(nums[1][2])

# a = int(input())
# b = int(input())
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# print(students[a])

# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# print(nums[1])

# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# print(nums[2][0])

# nums = [
#     [5, 10],
#     [15, 20]
# ]
# print(nums[0][0])

# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# print(nums[2][1])

# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for i in nums:
#     print(i)

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in nums:
#     for o in i:
#         print(o)

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in nums:
#     for o in i:
#         print(o, end=" ")

# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]
# for i in nums:
#     for o in i:
#         if o > 10:
#             print(o, end=" ")

# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]
# count=[]
# for i in nums:
#     count+=i
# print(len(count))

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in nums:
#     for o in i:
#         if o % 2 == 0:
#             print(o,end=" ")

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# count=[]
# for i in nums:
#     count+=i
# print(sum(count))

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in nums:
#     for o in i:
#         if o % 2 != 0:
#             print(o,end=" ")
    
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]
# a = 0
# for i in nums:
#     for o in i:
#         if o % 2 == 0:
#             a += o
# print(a)

# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]

# count = 0
# for i in nums:
#     for o in i:
#         if o > 0:
#             count += 1 

# print(count, end=" ")

# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]
# count = 0
# for i in nums:
#     for o in i:
#         if o < 0:
#             count += o

# print(count, end=" ")

# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]
# a = sum(nums, [])
# print(max(a))

# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ]
# a = sum(nums, [])
# print(min(a))

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in nums:
#     print(sum(i))

# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums:
#     print(max(i))

# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums:
#     print(min(i))

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# a = []
# for i in nums:
#     for o in i:
#         a.append(o)
# if 7 in a:
#     print("yes")
# else:
#     print("no")

# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]


