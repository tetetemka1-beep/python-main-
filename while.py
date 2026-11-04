
# i = 1000
# while i >0:
#     print(i)
#     i += 1000

# while True:
#     print("bnu")

# i = 1 
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 10
# while i >= 1 :
#     print(i)
#     i = i - 1

# a = 0
# i = 1
# while i <= 100:
#     a += i
#     i += 1
# print(a)

# too = 1 
# while too < 1000 :
#     print(too)
#     too *= 2

# i = 1
# while i <=5:
#     print(i)
#     i += 1
    
# i = 10
# while i >= 1:
#     i = i - 1
#     print(i)
# task 1
# i = 1
# n = int(input("togoo oruul "))
# while i <= n :
#     print(i)
#     i = i + 1
# task 2
# n = int(input("togoo oruul "))
# while n >= 1 :
#     print(n)
#     n = n - 1
# task 3
# n = int(input("togoo oruul "))
# i = 1
# while i <= n: 
#     if i % 2 == 0:
#         print(i) 
#     i = i +1
# task 4
# n = int(input("togoo oruul "))
# i = 1
# while i <= n: 
#     if i % 2 != 0:
#         print(i) 
#     i = i +1
# task 5

# n = int(input("too oruul: "))
# a = 0
# i = 1
# while i <= n:
#     a += i  
#     i += 1        
# print(a)
# task 6
# n = int(input("too oruul "))
# a = 0
# i = 1
# while i <= n:
#     i += 1
#     if i % 2 == 0:
#         a += i
#         print(a)
# task 7
# n = int(input("togoo oruul "))
# i = 1
# while i <= n: 
#     if i % 3 == 0:
#         print(i) 
#     i = i +1

# a = 0
# n = int(input("hussen togoo oruul  "))
# for i in range (1, n):
#     if i % 2 == 0:
#         print(i)

# task 8
# n = int(input("Heden too oruulah ve: "))
# positive = 0
# negative = 0
# zero = 0
# i = 1
# while i <= n:
#     too = int(input("Too oruul: "))
#     if too > 0:
#         positive += 1
#     elif too < 0:
#         negative += 1
#     else:
#         zero += 1
#     i += 1
# print("Eyereg too:", positive)
# print("Surug too:", negative)
# print("Teg:", zero)

# task 9
# n = int(input("Heden too oruulah ve: "))
# sum = 0
# i = 1
# while i <= n:
#     too = int(input("Too oruul: "))
#     if too > 0:
#         sum += too
#     i += 1
# print("Eyereg toonuudiin niilber:", sum)

# task 10

# n = int(input("Heden too oruulah ve: "))
# i = 1
# too = int(input("Too oruul: "))
# max_num = too
# while i < n:
#     too = int(input("Too oruul: "))
#     if too > max_num:
#         max_num = too
#     i += 1
# print("Hamgiin ih too:", max_num)

# task 11
# n = int(input("Heden too oruulah ve: "))
# i = 1
# too = int(input("Too oruul: "))
# min_num = too
# while i < n:
#     too = int(input("Too oruul: "))
#     if too < min_num:
#         min_num = too
#     i += 1
# print("Hamgiin baga too:", min_num)

# task 12
# n = int(input("Too oruul: "))
# i = 1
# while i <= n:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1
# task 13
# n = int(input("Buhel too oruul: "))
# n = abs(n)
# count = 0
# if n == 0:
#     count = 1
# while n > 0:
#     n = n // 10
#     count += 1
# print("Tsifriin too:", count)
# task 14
# n = int(input("Eyereg buhel too oruul: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n = n // 10
# print("Tsifruudiin niilber:", sum)
# task 15
# n = int(input("Eyereg buhel too oruul: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print("Urwuu too:", reverse)
# task 16
# n = int(input("Buhel too oruul: "))
# original = n
# n = abs(n)
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# if original >= 0 and original == reverse:
#     print("Palindrom too mun")
# else:
#     print("Palindrom too bish")
# task 17
# n = int(input("Buhel too oruul: "))
# i = 2
# count = 0
# while i < n:
#     if n % i == 0:
#         count += 1
#     i += 1
# if n > 1 and count == 0:
#     print("Anhnii too mun")
# else:
#     print("Anhnii too bish")
# task 18
# n = int(input("N too oruul: "))
# num = 2
# while num <= n:
#     i = 2
#     count = 0
#     while i < num:
#         if num % i == 0:
#             count += 1
#         i += 1
#     if count == 0:
#         print(num)
#     num += 1
# task 19
# n = int(input("Too oruul: "))
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", n * i)
#     i += 1
# task 20
# password = input("Nuuts ug oruul: ")
# while password != "python123":
#     print("Nuuts ug buruu baina!")
#     password = input("Dahin oruul: ")
# print("Nuuts ug zuv baina!")