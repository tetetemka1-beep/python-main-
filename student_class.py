# class student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age 
# student1 = student("naraa" , 17)
# student2 = student("temuulen" , 19)
# print(student1.name , student1.age)       
# print(student2.name , student2.age)

# task 2
# class student:
#     def __init__(self, name , age , clas):
#         self.name = name
#         self.age = age
#         self.clas = clas
# student1 = student("Бат", 18, "12А")   
# print(f"ner:{student1.name}")    
# print(f"nas:{student1.age}")
# print(f"angi:{student1.clas}") 

# task 3

# class student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score
# student1 = student("bat" , 85)
# student2 = student("saraa" , 95)
# print(student1.name , student1.score)
# print(student2.name , student2.score)

# task 4

# class student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
        
# student1 = student("bat" , 85)
# student2 = student("saraa" , 95)
# student1.add_score()
# student2.add_score()
# print(student1.name , student1.score)
# print(student2.name , student2.score)

# task 5

# class student:
#     def __init__(self , name , age , gg):
#         self.name = name 
#         self.age = age
#         self.gg = gg
#     def show_info(self):
#         print("ner:",self.name)
#         print("nas:", self.age)
#         print("angi:", self.gg)
# student1 = student("Сараа", 19, "12Б")
# student1.show_info()
    

# task 6

# class student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score
#     def check_result(self):
#         if self.score >= 60:
#             print(f"{self.name}: tentssen")
#         else:
#             print(f"{self.name}: tentseegui")

# student1 = student("Бат", 75)
# student2 = student("Нараа", 45)

# student1.check_result()
# student2.check_result()

# task 7
# class student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
# student1 = student("Бат", 80)
# student1.add_score()
# print(student1.score)

# task 8
# class student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#     def add_age(self):
#         self.age += 1
# student1 = student("Сараа", 18)
# student1.add_age()
# student1.add_age()
# print(student1.age)
# task 9
# class student:
#     def __init__(self ,name, score):\
#         self.score = score
#         self.name = name
#     def get_grade(self):
#         if 90 <= self.score <= 100:
#             print("A")
#         elif 80 <= self.score < 90:
#             print("B")
#         elif 70 <= self.score < 80:
#             print("C")
#         elif 60 <= self.score < 70:
#             print("D")
#         elif 0 <= self.score < 60:
#             print("F")
#         else:
#             print("onoo buruu baina")
# student1 = student("Бат", 95)
# student1.get_grade()
# task 10
# class student:
#     def __init__(self ,name, score , irts):
#         self.score = score
#         self.name = name
#         self.irts = irts
#     def attend(self):
#         self.irts +=1
#     def show(self):
#         print(self.irts)
# student1 = student("bat",70 , 0)
# student1.attend()
# student1.attend()
# student1.show()
# task 11
# class student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score
#     def check_result(self):
#         if self.score >= 60 and self.score <= 80:
#             print(f"{self.name}: tentssen")
#         else:
#             print(f"{self.name}: tentseegui")

# student1 = student("Бат", 75)
# student2 = student("Нараа", 45)

# student1.check_result()
# student2.check_result()

# task 12
# class student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score
#     def add_score(self , score):
#         self.score.append(score)
#     def show(self):
#         print(self.score)
#     def averaga(self):
#         print(sum(self.score) / (len(self.score)))
# student1 = student("Бат", [80, 90, 70])
# student1.add_score(100)
# student1.show()
# student1.averaga()

# task 13
# class student:
#     def __init__(self , name, angi):
#         self.name = name 
#         self.angi = angi
#     def show(self):
#         print(self.name , self.angi)
#     def change_name(self,new_name):
#         self.name = new_name
#     def change_angi(self,new_score):
#         self.angi = new_score
# student1 = student("Сараа",10)
# student1.change_name("bat")
# student1.change_angi(7)
# student1.show()

# task 14
# class Student:
#     def __init__(self, name, class_name):
#         self.name = name
#         self.class_name = class_name
#         self.scores = []
#     def show_info(self):
#         print("ner:", self.name)
#         print("angi:", self.class_name)
#         print("shalgaltiin onoo:", self.scores)
#     def add_score(self, score):
#         self.scores.append(score)
#     def check_result(self):
#         if len(self.scores) == 0:
#             print("onoo baihkuu bn.")
#         elif self.average() >= 60:
#             print("tentssen")
#         else:
#             print("tentseeguu")
#     def average(self):
#         if len(self.scores) == 0:
#             return 0
#         return sum(self.scores) / len(self.scores)
# student1 = Student("bat", "10a")
# student1.add_score(80)
# student1.add_score(70)
# student1.add_score(90)
# student1.show_info()
# print("dundaj onoo:", student1.average())
# student1.check_result()
