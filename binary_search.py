# def binary_search(items, target):
#     lo, hi = 0, len(items) - 1 # 1. хүрээ = бүх жагсаалт
#     while lo <= hi: # 2. хүрээ хоосон биш байхад
#         mid = (lo + hi) // 2 # 3. дунд индекс
#         if items[mid] == target: # 4а. олдлоо
#             return mid
#         elif items[mid] < target: # 4б. баруун талд байна
#             lo = mid + 1
#         else: # 4в. зүүн талд байна
#             hi = mid - 1
#     return -1 # 5. хүрээ хоосон → байхгүй

# nums = [2, 5, 8, 12, 16, 23, 38, 41, 56, 61, 67, 72, 80, 85, 91, 99]
# print(binary_search(nums, 67)) # 10
# print(binary_search(nums, 40))


# def binary_search_rec(items, target, lo=0, hi=None):
#     if hi is None:
#         hi = len(items) - 1 # анхны дуудлага: бүх жагсаалт
#     if lo > hi: # суурь тохиолдол: хүрээ хоосон
#         return -1
#     mid = (lo + hi) // 2
#     if items[mid] == target:
#         return mid
#     if items[mid] < target:
#         return binary_search_rec(items, target, mid + 1, hi)
#     return binary_search_rec(items, target, lo, mid - 1)

# task 1

# def binary_search(item,target):
#     lo = 0 
#     hi = len(item) - 1
#     while lo <= hi:
#         mid = (lo + hi)//2
#         if item[mid] == target:
#             print("olson")
#             break
#         elif item[mid] < target:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     print("olsonguu")
# item  = [3, 7, 12, 18, 25, 31, 40]
# item.sort()
# target = int(input())
# binary_search(item,target)

# task 2

# def binary_search(item,target):
#     lo = 0 
#     hi = len(item) - 1
#     while lo <= hi:
#         mid = (lo + hi)//2
#         if item[mid] == target:
#             return mid
#         elif item[mid] < target:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return -1
# item = [5, 10, 15, 20, 25, 30]
# target = int(input())
# binary_search(item,target)
# task 3
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return mid
#         elif l[mid] <= n:
#             left = mid +1
#         else:
#             right = mid - 1
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 4
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 5
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return "oldloo"
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#             return "haij bui too baihgui"
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# taks 6
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     a = 0
#     while left <= right:
#         a += 1
#         mid = (right + left) // 2
#         if l[mid] == n:
#             print("oldloo")
#             return a
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#             print("oldsongue")
#             return a
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 7
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#     return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 8
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return "Burtgeltei"
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#             return "burtgelgui"
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 9    
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#             return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 10
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     count = 0
#     while left <= right:
#         mid = (right + left) // 2
#
# print(left,right,mid)
#         count +=1
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#             return "oldsongue"
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 11
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     count = -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             count = mid
#             right = mid -1
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#     return count
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 12
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     count = -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             count = mid
#             left = mid +1
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#     return count
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 13
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#     return left
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 14
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     count = None
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] < n:
#             count = l[mid]
#             left = mid +1
#         else:
#             right = mid -1
#     if count is not None:
#         return count
#     else:
#         return "baihgui"
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 15
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     count = None
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] > n:
#             count = l[mid]
#             right = mid -1
#         else:
#             left = mid +1
#     if count is not None:
#         return count
#     else:
#         return "baihgui"
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 16
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#     return -1
# l = list(map(int, input().split()))
# n = int(input())
# a = int(input())
# print(linier(l,n))
# print(linier(l,a))

# task 17
# def linier(l,n):
#     l.sort()
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             return "oldloo"
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#             return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# # task 18
# def biniary_search(numbers, target):
#     left = 0
#     rigth = len(numbers) -1
#     while left <= rigth:
#         mid = (rigth + left) // 2
#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid +1
#         else:
#             rigth = mid -1
#             return -1
# numbers = list(map(int, input().split()))
# target= int(input())
# print(biniary_search(numbers,target))

# task 19
# def linier(l,n):
#     left = 0
#     right = len(l) -1
#     count = -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             count = mid
#             right = mid -1 
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#     return count
# def linieror(l,n):
#     left= 0
#     right = len(l) -1
#     count = -1
#     while left <= right:
#         mid = (right + left) // 2
#         if l[mid] == n:
#             count = mid
#             left = mid +1
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#     return count
# def counter():
#     l = list(map(int,input().split()))
#     n = int(input())
#     a = linier(l,n)
#     if a == -1:
#         print(n)
#         return
#     b = linieror(l,n)
#     w = b - a +1
#     print(n,w)
# counter()

# task 20
# def linior(l,n):
#     linior_steps = 0
#     for i in range(len(l)):
#         linior_steps += 1
#         if l[i] == n:
#             break
#     binary_steps = 0
#     left = 0
#     right = len(l) -1
#     while left <= right:
#         binary_steps += 1
#         mid = (right + left) // 2
#         if l[mid] == n:
#             break
#         elif l[mid] < n:
#             left = mid +1
#         else:
#             right = mid -1
#         print(f"{n} toog haisan ur dun")
#         print(f"{linior_steps} shuluun hailtiin ur dun")
#         print(f"{binary_steps} hoyr hsiltiin shalgasan ur dun")
#         print(f"ylgaa: {linior_steps - binary_steps}")
# a= list(map(int,input().split()))
# linior(a,38)

# task 21
# price = {"talh": 2500, "suu": 3200, "ondog": 450, "us": 1000, "alim": 1800}
# def a():
#     sags = {}
#     while True:
#         name = input("baraani neriig oruulnu: ").split()
#         if name == "toloh":
#             break
#         if name not in price:
#             print(f"{name} manai delguurt bhku")
#             continue
#         too = int(input("too shirheg oruulnu: "))
#         if too <= 0:
#             print("too shirheg buruu bn")
#             continue
#         if name in sags:
#             sags[name] += too
#         else:
#             sags[name] = too
# def b(sags):
#     niit = 0
#     for baraa, too in sags.items( ):
#         baraa_dun = price[baraa] * too
#         niit += baraa_dun
#         print(f"{baraa} x {too} = {baraa_dun}")
#         hongololt = 0
#         if niit >= 20000:
#             hongololt = niit * 0.10
#         toloh_dun = niit - hongololt
#         print("-" *25)
#         print(f"Niit dun: {niit}") 
#         print(f"hongololt: {hongololt}")
#         print(f"toloh dun: {toloh_dun}")