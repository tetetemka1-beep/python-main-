# task 1.1
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("oroj bolno.")
# else:
#     print("oroh bolhguu.")

# task 1.2

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# task 1.3
# a , b = map(int, input("2 too oruul: ").split())
# if a > b:
#     print("ih too:", a)
# else:
#     print("ih too:", b)

# task 1.4
# day = int(input("Enter a number (1-7): "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday(amraltiin odor)")
# elif day == 7:
#     print("Sunday(amraltiin odor)")
# else:
#     print("too oldson guu.")

# task 1.5

# km , hour = map(int,input().split())
# if km <= 2:
#     price = 3000
# else:
#     price = 3000 + (km-2) * 1500
# if hour >= 22 or hour < 6:
#     price = int(price * 1.2)
# print(price)

# task 1.6

# kwh = int(input("kwh oruul "))
# if kwh <= 150:
#     bill = kwh * 100
# elif kwh <= 300:
#     bill = (150 * 100) + ((kwh - 150) * 150)
# else:
#     bill = (150 * 100) + (150 * 150) + ((kwh - 300) * 200)
# print(bill)

# task 2.1
# n = int(input())
# for i in range(1,n+1):
#     print(i)

# task 2.2

# n = int(input())
# a = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         a += i
# print(a)

# task 2.3
# n = int(input())
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# task 2.4

# n = 10000
# j = 0 
# while n <= 2000000:
#     n = n * 0.12 + n
#     j +=1
# print(j)

# task 2.5

# number = int(input("too oruul "))
# if number <= 1:
#     print(f"{number} -> {number} bish ")
# else:
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print(f"{number} -> {number} bish, {i}-т huvaagdan")
#             break
#     else:
#         print(f"{number} -> {number} ahnii too")

# task 2.6

# for i in range(1,21):
#     if i % 3 == 0 :
#         continue
#     print(i , end=" ")

# task 2.7 

# n = 4
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# task 2.8
# secret = 42
# max_attempts = 5
# won = False
# for i in range(1, max_attempts + 1):
#     num = int(input(f"{i}-р оролдлого (Тоогоо оруулна уу): "))
    
#     if num > secret:
#         print(f"{num}: Их байна")
#     elif num < secret:
#         print(f"{num}: Бага байна")
#     else:
#         print(f"{num}: Зөв! {i} дахь оролдлогоор таалаа")
#         won = True
#         break
# if not won:
#     print(f"Ялагдлаа. Нууц тоо: {secret}")

# task 2.9
# n = int(input())
# while n >= 10:
#     a = 0 
#     while n > 0 :
#         a += n % 10
#         n //= 10
#     n = a
# print(a)

# task 3.1

# a = [80, 90, 70, 60]
# b = (sum(a)/len(a))
# c = sum(a)
# print(f"nillber -> {c} dundaj -> {b} ")

# task 3.2
# n = [45, 89, 72, 89, 30]
# max_value = n[0]
# max_index = 0
# for i in range(1, len(n)):
#     if n[i] > max_value:
#         max_value = n[i]
#         max_index = i
# print(f"hamgiin ih: {max_value} index : {max_index}")

# task 3.3

# names = ["bat", "bold", "saraa"]
# n = str(input())
# if n in names:
#     indexs = names.index(n)
#     print(f"oldson {indexs}")
# else:
#     print("oldsonguu")

# task 3.4

# prices = list(map(int,input().split()))
# b = []
# for p in prices:
#     new_price = int(p * 0.9)
#     b.append(new_price)
# print(b)

# word = "python"
# print(word.capitalize())

# def linear(a, b):
#      for i in range(len(a)):
#         if a[i] == b: return i
#         return -1
# a = list(map(int,input().split()))
# b = int(input())
# result = linear(a,b)
# print(result)
# task 3.5
# a = [45, 78, 60, 30, 92]
# student = []
# for score in a:
#     if score >= 60:
#         student.append(score)
# print(student)
# print(f"Tentssen: {len(student)}")

# task 3.6
# a = list(map(int, input().split()))
# total = 0
# for n in a:
#     if n >= 5000:
#         total += n + 2000
# print(total)
# a = list(map(int, input().split()))
# b = sum([n + 2000 for n in a if n >= 5000])
# print(b)

# task 3.7
# names = ["Bat", "Saraa", "Dorj"]
# subject = ["Matematik", "Pizik", "Angli hel", "Tuuh"]
# scores = [
#     [80,90,70,60],
#     [95,85,75,65],
#     [50,60,70,80]
# ]
# print("1.dundaj onoo:")
# for i in range(len(names)):
#     avg_scores = sum(scores[i]) / len(scores[i])
#     print(f"{names[i]}: {avg_scores}")
# print("\n2. hicheel buriin hamgiin ondor onoo")
# for subject, sub_scores in zip(subject, zip(*scores)):
#     max_score = max(sub_scores)
#     max_index = sub_scores.index(max_score)
#     top_student = names[max_index]
#     print(f"{subject}: {top_student} ({max_score})")

# task 4.1
# text = "batbold"
# a = text[0].upper() + text[1:]
# b = len(text)
# print(f"{a} ({b} useg)")

# task 4.2
# name = input()
# oloh = input()
# count = 0
# for c in name:
#     if c == oloh:
#         count+= 1
# print(count)
# a = name.count(oloh)
# print(a)

# task 4.3
# a = input()
# if a.count("@") != 1:
#     print("buruu imail")
# else:
#     username, domain = a.split("@")
#     if len(username) == 0 or "." not in domain or domain.endswith("."):
#         print("buruu imail")
#     else:
#         print(f"Username: {username}, domain: {domain}")

# task 4.4
# bad_words = ["muu", "teneg"]
# b = input()
# words = b.split()
# a = []
# for word in words:
#     v = word.lower()
#     is_bad = False
#     for bad in bad_words:
#         if bad in v:
#             word = "*" *len(word)
#             break
#     a.append(word)
# n = " ".join(a)
# print(n)

# task 4.5
# a = input()
# cleaned = "".join([c.lower() for c in a if c.isalnum()])
# palindrom = cleaned == cleaned[::-1]
# print(palindrom)

# task 5.1
# def square(n):
#     return n ** 2
# print(square(-3))

# task 5.2
# def greet(name = "Zochin"):
#     return f"Sain uu {name}!"
# print(greet("Bat"))
# print(greet())

# task 5.3
# def is_adult(age):
#     return age >= 18
# print(is_adult(20))
# print(is_adult(16))

# task 5.4
# def calculate_bmi(weight,height):
#     bmi =  weight / (height * height)
#     return round(bmi, 2)
# def get_category(bmi):
#     if bmi <= 18.5:
#         return "Turanhai"
#     elif bmi <= 25:
#         return "Hewiin"
#     elif bmi <= 30:
#         return "iluudel jintei"
#     else:
#         return "Targalaltai" 
# w1,h1 = 70, 1.75
# bmi1 = calculate_bmi(w1,h1)
# cat1 = get_category(bmi1)
# print(w1,h1,bmi1,cat1)

# w2,h2 = 95, 1.70
# bmi2 = calculate_bmi(w2, h2)
# cat2 = get_category(bmi2)
# print(w2,h2,bmi2,cat2)

# task 5.5
# def calc_insurance(gross):
#     return gross * 0.115
# def calc_tax(gross):
#     ndsh = calc_insurance(gross)
#     return (gross - ndsh) * 0.10
# def calc_net(gross):
#     ndsh = calc_insurance(gross)
#     tax = calc_tax(gross)
#     net = gross - ndsh - tax
#     return net
# gross_salary = 2000000
# print(f"gross = {gross_salary}")
# print(f"ndsh: {int(calc_insurance(gross_salary))}")
# print(f"tatvar: {int(calc_tax(gross_salary))}")
# print(f"gart: {int(calc_net(gross_salary))}") 

# task 5.6
# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     def decrement():
#         nonlocal count
#         count -=1
#         return count
#     def reset():
#         nonlocal count
#         count = 0
#         return count
#     return{
#             "increment": increment,
#             "decrement": decrement,
#             "reset": reset
#     }
# c1 = make_counter()
# c2 = make_counter()
# print(c1["increment"]())
# print(c1["increment"]())
# print(c2["increment"]())
# print(c1["decrement"]())
# print(c1["reset"]())

# task 6.1
# a = {"name": "Bat",
#      "age": 20,
#      "city": "Ulaanbaatar"}
# a["age"] +=1
# a.update({"email":"bat@gmail.com"})
# del a["city"]
# print(a)

# task 6.2
# prices = {"talh": 2500, "suu": 3800, "mah": 18000}
# for key,value in prices.items():
#     print(key,value)

# task 6.3
# prices = {"talh": 2500, "suu": 3800, "mah": 18000, "ondog": 6500}
# max_name = ""
# max_une = 0
# total = 0
# for baraa,une in prices.items():
#     total += une
#     if une > max_une:
#         max_une = une
#         max_name = baraa
# print(f"Hamgiin unetei mah: {max_name} - {max_une}")
# print(f"Niit: {total}")

# task 6.4
# votas= ["Bat", "Saraa", "Bat", "Dorj", "Bat", "Saraa"]
# total = {}
# for name in votas:
#     total[name] = total.get(name, 0) +1
# print(total)
# winner = ""
# max_votes = 0
# for name , count in total.items():
#     if count > max_votes:
#         max_votes = count
#         winner = name
# print(f"Winner: ({max_votes} sanal)")

# task 6.5
# students = [
#     {"name": "bat", "class": "10A", "score":85},
#     {"name": "Saraa", "class": "10B", "score":92},
#     {"name": "Dorj",     "class": "10A", "score": 70},
#     {"name": "Naraa",    "class": "10B", "score": 78},
#     {"name": "Temuulen", "class": "10A", "score": 95},
# ]
# group = {}
# for s in students:
#     cls = s["class"]
#     name = s["name"]
#     if cls not in group:
#         group[cls] = []
#     group[cls].append(name)
# print(group)

# task 6.6
# students = [
#     {"name": "bat", "class": "10A", "score":85},
#     {"name": "Saraa", "class": "10B", "score":92},
#     {"name": "Dorj",     "class": "10A", "score": 70},
#     {"name": "Naraa",    "class": "10B", "score": 78},
#     {"name": "Temuulen", "class": "10A", "score": 95},
# ]
# class_data = {}
# for s in students:
#     cls = s["class"]
#     name = s["name"]
#     score = s["score"]
#     if cls not in class_data:
#         class_data[cls] = [0,0, "", 0]
#     class_data[cls][0] += score
#     class_data[cls][1] += 1
#     if score > class_data[cls][3]:
#         class_data[cls][2] = name
#         class_data[cls][3] = score
# for cls, data in class_data.items():
#     total = data[0]
#     count = data[1]
#     student = data[2]
#     max_score = data[3]
#     avg = total / count
#     print(cls,avg,student,max_score)