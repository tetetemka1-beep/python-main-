# daalgavar
# 1
# a = [3,4,5]
# print(sum(a))
# 2
# a, b, = map(int,input("2 too oruul ").split())
# print("hariu: ",a+b)
# 3
# a = int(input("tegsh ontsogt "))
# print(a**3,6*a**2)
# 4
# a , b , = map(int,input("2 too oruul ").split())
# print(a*b, (a+b)*2)
# 5
# a = int(input("too oruul "))
# print("y=" ,3*a-5)
# 6
# a = int(input("too oruul "))
# print("y= " ,4*a*a-3*a+5)
# 7
# a = int(input("too oruul "))
# print("hariu ", a%10)
# 8
# a = int(input("too oruul "))
# print((a//10)%10)
# 9
# a = int(input("too oruul "))
# print((a//10)*(a%10))
# 10
# a = int(input("too oruul "))
# print((a//3600),(a%3600)//60,(a%100))
# 11
# a, b, c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split())
# print(a*3600+b*60+c)
# 12
# b, c = map(int,input("zaigaar tusgaarlan 2 too oruul : ").split())
# print(b*60+c)
#  13
# h = int(input())
# day = h // 24
# hour = h % 24
# print(f"{day} {hour}")
# 14
# honog, tsag = map(int,input("odr honogoo oruul daa ").split())
# a = honog * 24 + tsag
# print(a)
# 15
# s = int(input())
# j = s // 12
# k = s % 12
# print(f"{j} {k}")
# 16
# jil, sar = map(int,input("sar jil  ").split())
# a = jil * 12 + sar
# print(a)
# 17
# a = map(int,input().split())
# print(max(a))
# 18
# a = map(int,input().split())
# print(min(a))
# 19
# a = map(int,input().split())
# print(max(a))
# 20
# a = map(int,input().split())
# print(min(a))
# 21
# a = map(int,input().split())
# print(sum(a))
# 22
# n = list(map(int, input().split()))
# p = 1
# for i in n :
#     if i < 5:
#         p *= i
# print(p)
# 23
# n = list(map(int, input().split()))
# e = sum( n for n in n if n % 2 == 0)
# print(e)
# 24
# n = list(map(int,input().split()))
# e = 1
# for i in n:
#     if i % 2 != 0 :
#         e *= i
# print(e)
# 25
# a = list(map(int,input().split()))
# print(a.count(5))
# 26

# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if i % 3 == 0:       
#         b += 1       
# print(b)
# 27
# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if i % 11 != 0:      s
#         b += i       
# print(b)
# 28
# a = list(map(int,input().split()))
# for i in a:
#     if i > 10 :
#         print("yes")
#     else:
#         print('no')
# 29
# a = int(input())
# if a < 5:
#     print("yes")
# else:
#     print("no")
# 30
# for _ in range(3):
#     n = int(input())
#     if n % 2 == 0:
#         print("YES")
#     else:
#         print("NO")
# 31
# print("IOI")
# 32
# for i in range(3):
#     print("IOI")
# 33
# n = int(input())
# b = 0
# for i in range(1, n + 1):
#     b += i
# print(b)
# 34
# n = int(input())
# a = 1
# for i in range(1,n+1):
#     a *= i
# print(a)
# 35
# n =int(input())
# a = 0
# for i in range(n):
#     a += 100
# print(a)
# 36
# a , b = map(int,input().split())
# n = 0 
# for i in range(b):
#     n += a
# print(n)
# 37
# n = 2 
# a = int(input())
# l = n ** a
# print(l)
# 38
# a , b = map(int,input().split())
# j = a ** b
# print(j)
# 39
# n = int(input())
# if n >= 3:
#     print("tentssen")
# else:
#     print("tentseegui")
# 40
# dun = int(input())
# if dun == 5:
#     print("Onts")
# elif dun == 4:
#     print("Sain")
# elif dun == 3:
#     print("Dund")
# elif dun == 2:
#     print("Muu")
# 41
# n = int(input())
# if n == 1:
#     print("Monday")
# elif n == 2:
#     print("Tuesday")
# elif n == 3:
#     print("Wednesday")
# elif n == 4:
#     print("Thursday")
# elif n == 5:
#     print("Friday")
# elif n == 6:
#     print("Saturday")
# elif n == 7:
#     print("Sunday")
# else:
#     print("tiim odr bhkuu")
# 42
# n = int(input())
# if 2 <= n <= 4:
#     print("Spring")
# elif 5 <= n <= 7:
#     print("Summer")
# elif 8 <= n <= 10:
#     print("Autumn")
# else:
#     print("Winter")
# 43
# a, b, c  = map(int,input().split())
# if a + b > c and a + c > b and b + c > a:
#     print("yes")
# else:
#     print("no")
# 44
# n = int(input())
# for i in range(1, 11):
#     print(f"{n}*{i}={n*i}")
# 45
# a, n,  = map(int,input().split())
# h = 1
# for i in range (1 , n+1):
#     h = a ** i
# print(f"{a}*{i}={h}")
# 46
# b, c, d = map(int, input().split())
# print(b * c - d)
# 47
# d, a = map(int, input().split())
# h = int(input())
# s = h % a
# if s == 0:
#     print(f"{h // a} {a}")
# else:
#     print(f"{(h // a) + 1} {s}")
# 48
# f, e, a = map(int, input().split())
# h = int(input()) - 1
# p= f * a
# j = (h // p) + 1
# i = h % p
# o = (i // a) + 1
# k = (i % a) + 1
# print(f"{j} {o} {k}")
# 49
# n = int(input())
# print(n * (n + 1) // 2)
# 50
# n = int(input())
# print(n * (n + 1) * (2 * n + 1) // 6)
# 51
# n = int(input())
# a = 0
# for i in range(1, n+1, 2):
#     a=a+i
# print(a)
# 52
# n = int(input())
# while n >= 10:
#     n //= 10
# print(n)
# 53
# a = int(input())
# b = (a // 100) + ((a // 10) % 10) + (a % 10)
# print(b)
# b = map(int, input().split())
# a = 0
# while b % 2 == 0:
#     if b > 0:
#         b = b + a % 10
#         a //= 10
# print(b)
# 54
# n = 0
# t = 0
# z = int(input())
# k = z
# while k > 0:
#     i = k % 10
#     if i % 2 == 1:
#         t += 1
#     n = n + i
#     k = k // 10
# print(t)
# 55
# z, x = map(int, input().split())
# k = z
# t = 0

# while k > 0:
#     i = k % 10
#     if i == x:
#         t += 1
#     k = k // 10
# print(t)
# 56
# n = int(input())
# s = 0
# while n > 0:
#     if s < n % 10:
#         s = n % 10
#     n = n // 10
# print(s)
# 57
# n = int(input())
# s = 10
# while n > 0:
#     if n % 10 < s: 
#         s = n % 10
#     n //= 10
# print(s)
# 58
# n = int(input())
# r = 0
# while n != 0:
#     a = n % 10
#     r = r * 10 + a
#     n //= 10
# print(r)
# 59
# z = int(input())
# k = z
# n = 0
# while k > 0:
#     i = k % 10
#     n = n * 10 + i
#     k = k // 10
# if n == z:
#     print("YES")
# else:
#     print("NO")
# 60
# a = int(input())
# b = 1
# while b < a:
#     b = b * 2
# if a == b:
#     print("YES")
# else:
#     print("NO")
# 61
# a = int(input())
# while a % 3 == 0:
#     a //= 3
# print(a)
# 62
# a, b = map(int, input().split())
# i = a
# while i > 0:
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break  
#     i -= 1
# 63
# a, b = map(int, input().split())
# x, y = a, b
# while y != 0:
#     x, y = y, x % y
# 64
# n = int(input())
# for i in range(1, n + 1):
#     print(n, end="")
# 65
# a = int(input())
# for i in range(a):
#     print(i, end=" ")
# 66
# n = int(input())
# i = 9
# while i >= n:
#     print(i)
#     i -= 1  
##############################################################################################
# 1
# a, b, c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split())

# # a=3
# # b=4
# # c=5
# print(" hariu :",a+b+c)
# 2
# a, b, = map(int,input("2 too oruul ").split())
# print("hariu: ",a+b)
# 3
# a = int(input("tegsh ontsogt "))
# print(a**3,6*a**2)
# 4
# a , b , = map(int,input("2 too oruul ").split())
# print(a*b, (a+b)*2)
# 5
# a = int(input("too oruul "))
# print("y=" ,3*a-5)
# 6
# a = int(input("too oruul "))
# print("y= " ,4*a*a-3*a+5)
# 7
# a = int(input("too oruul "))
# print("hariu ", a%10)
# 8
# a = int(input("too oruul "))
# print((a//10)%10)
# 9
# a = int(input("too oruul "))
# print((a//10)*(a%10))
# 10
# a = int(input("too oruul "))
# print((a//3600),(a%3600)//60,(a%10))
# 11
# a, b, c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split())
# print(a*3600+b*60+c)
# 12
# b, c = map(int,input("zaigaar tusgaarlan 2 too oruul : ").split())
# print(b*60+c)
# 13
# a = int(input("too oruul "))
# b=a//100
# c=(a//10)%10
# d=a%10
# print((d*100)+(c*10)+(b))
# 14
# a = int(input("too oruul "))
# b=a//100
# n=(a//10)%10
# m=a%10
# print(b*n*m)
# 15
# a = int(input("too oruul "))
# print((a//10)%10)
# 16
# a = int(input("too oruul "))
# b=a//100
# n=a%10
# print(b+n)
# 17
# a = int(input("too oruul "))
# b=a//100
# n=(a//10)%10
# m=a%10
# print(b,n,m,)
# 18
# a = int(input("too oruul "))
# b=a//100
# n=(a//10)%10
# m=a%10
# print(b,n,m,)
# 19
# a = int(input("too oruul "))
# b=a//1000
# n=(a//10)%10
# m=a%10
# z=(a//100)%10
# print(b,z,n,m,)
# 20
# n = int(input("too oruul "))
# t=n//1000
# f=n%1000//500
# h =n%500//100
# print(t, f,h)
# 21
# b, c = map(int,input("zaigaar tusgaarlan 2 too oruul : ").split())
# print(c,b)
# 22
# n = int(input("too oruul "))
# print((n%10)*10+n//10)
# 23
# a=int(input())
# b=a//100
# n=a%100
# print(b,n)
# 24
# a=int(input())
# p=a//1440
# b=a%1440//60
# c=a%60
# print(p,b,c,)
# 25
# a = int(input("too oruul "))
# l=(a//1000)
# b=(a//1000)//100
# n=(a//10)%10
# m=a%10
# print(l, b, n, m,)