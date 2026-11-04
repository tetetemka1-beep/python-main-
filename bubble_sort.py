#  task 1
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 2
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]<numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 3
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 4
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 5
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers , end=" ")
# task 6
# numbers = list(map(str,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 7
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 8
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     if numbers[i]>numbers[i+1]:
#         temp = numbers[i]
#         numbers[i]=numbers[i+1]
#         numbers[i+1]=temp
# print(numbers)
# task 9
# numbers = list(map(int,input().split()))
# dav = 0
# for i in range(len(numbers)-1):
#     dav += 1
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(f"{numbers}, {dav}")
# task 10 
# numbers = list(map(int,input().split()))
# dav = 0
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
#             dav +=1
# print(f"{numbers} , {dav}")
# task 11
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers[-2])
# task 12
# numbers = list(map(str,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 13
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
#             print(numbers)
# task 14
# numbers = list(map(int,input().split()))
# sorted = True
# for i in range(len(numbers)-1):
#     swapped = False
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
#             sorted = False
#             swapped = True
            
#     if swapped == False:
#         break
# if sorted:
#     print("psda")
# print(numbers)
# task 15
# numbers = list(map(int,input().split()))
# round = 0
# for i in range(len(numbers)-1):
#     swapped = False
#     round += 1
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
            
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
#             swapped = True
#     if not swapped:
#         break
# print(numbers , round)
# task 16
# students = [
#     ["Bat", 75],
#     ["Saraa", 92],
#     ["Anu", 60],
#     ["Bold", 88]
# ]
# for i in range(len(students)-1):
#     for j in range(len(students)-1):
#         if students[j][1]>students[j+1][1]:
#             temp = students[j]
#             students[j]=students[j+1]
#             students[j+1]=temp
# print(students)
# task 17
# people = [
#     ["Bat", 19],
#     ["Anu", 17],
#     ["Bold", 21],
#     ["Saraa", 18]
# ]
# for i in range(len(people)-1):
#     for j in range(len(people)-1):
#         if people[j][1]>people[j+1][1]:
#             temp = people[j]
#             people[j]=people[j+1]
#             people[j+1]=temp
# print(people)
# print(f"hamgiin zaluu :{people[0]} , hamgiin hogshin :{people[-1]}")
# task 18
# numbers = list(map(int,input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j]>numbers[j+1]:
#             temp = numbers[j]
#             numbers[j]=numbers[j+1]
#             numbers[j+1]=temp
# print(numbers)
# task 19
# numbers = list(map(int, input().split()))

# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1):
#         if numbers[j] > numbers[j+1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j+1]
#             numbers[j+1] = temp
# print(numbers)
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] == 4:
#         count += 1
# print("4 too", count, "udaa baina.")

# task 20
# products = [
#     ["Mouse", 25000],
#     ["Keyboard", 65000],
#     ["USB", 12000],
#     ["Headphone", 80000]
# ]
# for i in range(len(products)-1):
#     for j in range(len(products)-1):
#         if products[j][1] < products[j+1][1]:
#             temp = products[j]
#             products[j] = products[j+1]
#             products[j+1] = temp
# for i in range(3):
#     print(products[i][0], products[i][1])
#task 21
# a = list(map(int,input().split()))
# for i in range(len(a)-1):
#     for j in range(len(a)-1 -i):
#         if a[j] > a[j + 1]:
#             temp = a[j]
#             a[j] = a[j + 1]
#             a[j + 1] = temp
# print(a)

#task 22
# a = input().split()
# for i in range(len(a)-1):
#     for j in range(len(a)-1 -i):
#         if len(a[j]) > len(a[j + 1]):
#             temp = a[j]
#             a[j] = a[j + 1]
#             a[j +1] = temp
# print(a)

#task 23
# a = list(map(int,input().split()))
# for i in range(len(a)):
#     if a[i] < a[0]:
#         temp = a[0]
#         a[0] = a[i]
#         a[i] = temp
# print(a)

#task 24
# a = list(map(int,input().split()))
# j = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0 :
#         temp = a[i] 
#         a[i] = a[j]
#         a[j] = temp
#         j += 1
# print(a)

#task 25
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c = a + b 
# for i in range(len(c)-1):
#     for j in range(len(c)-1 -i):
#         if c[j] > c[j + 1]:
#             temp = c[j]
#             c[j] = c[j + 1]
#             c[j + 1] = temp
# print(c)

#task 26
# def buble(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n -1):
#         round = 0
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 count +=1
#                 round +=1
#                 print(round)
#     return arr, count
# numbers = list(map(int,input().split()))
# print(buble(numbers))

#task 27
# n = [18, 5, 12, 3, 25, 9, 7]
# for  i in range(len(n)-1):
#     for j in range(len(n)-1 -i):
#         if n[j] > n[j + 1]:
#             temp = n[j]
#             n[j] = n[j + 1]
#             n[j + 1] = temp
# print(n[2])

#task 28
# n = [
#     ["Bat", 85],
#     ["Anu", 92],
#     ["Bold", 85],
#     ["Saraa", 70],
#     ["Temuulen", 92]
# ]
# for  i in range(len(n)):
#     for j in range(len(n)-1 -i):
#         if n[j][1] < n[j + 1][1]:
#             temp = n[j]
#             n[j] = n[j + 1]
#             n[j + 1] = temp
# print(n)

#task 29
# numbers = [3, 1, 4, 2, 5]
# count = 0 
# swap = 0
# for i in range(len(numbers)):
#     for j in range(len(numbers)-1 -i):
#         count += 1
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             swap += 1
#     if swap == 0:
#         print("soliltsoo xiigeegv")
#         break
# print("xaritsulalt:", count)
# print("soliltsoo:", swap)
# print("jagsaalt:", numbers)

#task 30
# products = [
#     ["Mouse", 25000, 12],
#     ["Keyboard", 65000, 5],
#     ["USB", 12000, 20],
#     ["Headphone", 65000, 8],
#     ["Webcam", 40000, 3]
# ]

# n = len(products)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if products[j][1] < products[j + 1][1] or (
#             products[j][1] == products[j + 1][1]
#             and products[j][2] > products[j + 1][2]
#         ):
#             temp = products[j]
#             products[j] = products[j + 1]
#             products[j + 1] = temp

# print(products)
