# task1
# a = ("ulaan" , "nogoon", "shar")
# print(a)
# task 2
# a = ("nohoi", "muur", "tuulai", "mori")
# b,c,d,f=a
# print(b,d,f)
# task 3
# a = (100,)
# print(type(a))
# task 4
# a = ("math", "mongol" ,"angil" , "python")
# print(f"{a[0]}\n{a[2]}\n{a[3]}")
# task 5
# a = (10, 20, 30, 40, 50)
# print(a[:3])
# task 6
# a = (10, 20, 30, 40, 50)
# print(a[-3:])
# task 7
# fruits = ("алим", "банана", "жүрж", "усан үзэм")
# print(len(fruits))
# task 8
# a = (45, 12, 89, 23, 7)
# print(max(a) , min(a) )
# task 9
# a = (80, 90, 70, 100)
# print(sum(a), sum(a)/len(a))
# task 10
# a = (50, 10, 40, 20, 30)
# print(sorted(a))
# task 11
# a = (10, 20, 10, 30, 10, 40)
# print(a.count(10))
# task 12
# b = ("алим", "банана", "жүрж", "усан үзэм")
# a = b.index("жүрж")
# print(a)
# task 13
# a = ("dog", "cat", "rabbit")
# b = input("animal: ")
# if b in a:
#     print("yes")
# else:
#     print("no")
# task 14
# student = ("Ану", 12, "7А")
# name, age, student_class = student
# print(f"ner :{name}\n nas: {age}\n class: {student_class}\n") 
# task 15
# coordinate = (15, 25)
# x , y = coordinate
# print(f"x = {x}\ny = {y}\n")
# task 16
# book = ("Python surah", "bat", 250)
# nom, zohiolch , huudas = book
# print(f"nom : {nom}\nzohiolch : {zohiolch}\nhuudas : {huudas}")
# task 17
# a = 5
# b = 10
# a, b = b, a
# print(f"a = {a}")
# print(f"b = {b}")
# task 18
# numbers = (10, 20, 30, 40, 50)
# first, *others = numbers
# print(f"ehnii utga: {first}")
# print(f"uldsen utga: {others}")
# task 19
# numbers = (1, 2, 3, 4, 5, 6)
# first, *middle, last = numbers
# print(f"ehnii too: {first}\nuldsen: {middle}\nsuulchiih: {last}")
# task 20
# student = ("Тэмүүлэн", "Математик", "Python", "Англи хэл")
# name, *hicheel = student
# print(f"ner: {name}\nhicheeluud: {hicheel}")
# task 21
# product = ("Дэвтэр", 3500, 4)
# name, price, quantity = product
# niit = price * quantity
# print(f"baraa: {name}\nune: {price}\nshirheg: {quantity}\nniit une: {niit}")
# task 22
# students = (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )
# for name, score in students:
#     print(f"{name}: {score}")
# task 23
# students = (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )
# for name, score in students:
#     if score >= 80:
#         print(name)
# task 24
# colors = ("улаан", "ногоон", "цэнхэр")
# color_list = list(colors)
# color_list.append("шар")
# tuple(color_list)
# print(color_list)