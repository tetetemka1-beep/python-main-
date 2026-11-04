# task1
# n = int(input())
# m = int(input())

# for i in range(1, n + 1):
#     niit = 0

#     for j in range(1, m + 1):
#         dun = int(input())
#         niit += dun

#     dundaj = niit / m

#     print(f"{i}-r suragch: niit {niit}, dundaj {dundaj}")

#     if dundaj >= 60:
#         print("tsentssen")
#     else:
#         print("tsentseeguu")
# task2
# n = int(input())

# for i in range(1, n + 1):
#     m = int(input())
#     niit = 0

#     for j in range(1, m + 1):
#         une = int(input())
#         shirheg = int(input())

#         niit += une * shirheg

#     mongo = int(input())

#     print(f"{i}-r hunii toloh dun: {niit}")

#     if mongo >= niit:
#         hariult = mongo - niit
#         print("hariult:", hariult)
#     else:
#         dutuu = niit - mongo
#         print("dutuu mongo:", dutuu)
# task3
# n = int(input())

# for i in range(1, n + 1):
#     tsalin = 0

#     for j in range(1, 6):
#         tsag = int(input())

#         if tsag <= 8:
#             tsalin += tsag * 5000
#         else:
#             tsalin += 8 * 5000
#             tsalin += (tsag - 8) * 7500

#     print(f"{i}-r ajiltnii tsalin: {tsalin}")
# task4
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     ur = int(input())
#     niit = 0

#     for j in range(1, m + 1):
#         tulbur = int(input())

#         ur -= tulbur
#         niit += tulbur

#         print(f"{i}-r hun, {j}-r sariin daraah uldegdel: {ur}")

#     print("niit tulsun:", niit)
# task5
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     niit = 0

#     for j in range(1, m + 1):
#         too = int(input())
#         niit += too

#     hairtsag = niit // 12
#     uldegdel = niit % 12

#     print(f"{i}-odr: niit {niit}, buten hairtsag {hairtsag}, uldegdel {uldegdel}")
# task6
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     hun = 0
#     niit = 0

#     for j in range(1, m + 1):
#         buusan = int(input())
#         suusan = int(input())

#         hun = hun - buusan
#         hun = hun + suusan

#         niit += suusan

#         print(f"{j}-r buudaliin daraa: {hun} hun")

#     orlogo = niit * 1000

#     print(f"{i}-r niit suusan: {niit}")
#     print("aylliin orlogo:", orlogo)
# task7
# n = int(input())

# for i in range(1, n + 1):
#     too = 0
#     niit = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             too += 1
#             niit += j

#     print(f"{i}: {too} huvsagchtai niilber {niit}")
# task8
# n = int(input())
# too = 0
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i + j == n:
#             print(f"{i} + {j} = {n}")
#             too += 1
# print("niit:", too, "hos")
# task9
# n = int(input())

# too = 0
# mungu = n // 1000

# for i in range(0, mungu + 1, 2):
#     uldegdel = mungu - i

#     if uldegdel >= 0:
#         print(f"1000₮: {uldegdel} shirheg, 2000₮: {i // 2} shirheg")
#         too += 1

# print("niit:", too, "huvilbar")
# task10
# n = int(input())
# too = 0
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i * j == n:
#             yalgaa = j - i
#             print(f"{i} x {j} = {n}, ylgavar {yalgaa}")
#             too += 1
# print("niit:", too, "hos")
