# task 1
# name= input("neriig chin hen gediin ")
# print(name , "sainu")
# task2
# b, c = map(int,input("zaigaar tusgaarlan 2 too oruul : ").split())
# print(b+c)
# task3
# b, c = map(int,input("zaigaar tusgaarlan 2 too oruul : ").split())
# print(b*c)
# task4
# a = int(input("too oruul "))
# print(a*2)
# task5
# a = int(input("nasaa oruul "))
# print(a+1)
# task6
# a = int(input("C oruul "))
# print(a*9/5+32)
# task7
# a = int(input("tooo oruul "))
# b= a//10
# c= a%10
# print(b+c)
# task8
# a = int(input("tooo oruul"))
# b=a//60
# c=(a%60)
# print(b ,c)
# task 9
# a = int(input("too oruul "))
# b=a//60
# c=a%10
# print(b,c)
# task 11
# a = int(input("too oruul "))
# if a < 0:
#     print("nagtive")
# else:
#     print("posituve")
# task 12
# a = int(input("too oruul "))
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
# task 13
# age = int(input("nasaa oruul "))
# if age>=18:
#     print("adult")
# else:
#     print("child")
# task 14
# b, c = map(int,input("zaigaar tusgaarlan 2 too oruul : ").split())
# if b > c:
#     print(b)
# else:
#     print(c)
# task 15
# a, b, c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split())
# if c > a and c > b:
#     print("yes")
# else:
#     print("no")
# task 16
# dun =  int(input("dungee oruul "))
# if dun < 0 or dun > 100:
#     print("inviad dun")
# elif dun >= 90:
#     print("A")
# elif dun >=80:
#     print("B")
# elif dun >=70:
#     print("C")
# elif dun>=60:
#     print("D")
# else:
#     print("F")
# task 17
# a = int(input("too oruul "))
# if a % 3 == 0:
#     print("yes")
# else:
#     print("no")
# task 18
# a, b, c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split())
# if a < b and a < c:
#     print(a)
# if b < a and b < c:
#         print(b)
# if c < a and c < b:
#         print(c)
# task 19
# a = int(input("too oruul "))
# if 10 <= a <= 50:
#     print("yes")
# else:
#     print("no")
# task 20
# age = int(input("nasaa oruul "))
# if age<=12:
#     ticket=input("ticket shalguul ")
#     if ticket == "baigaa":
#          print("orj bolno")
#     else:
#         print("ticket heregtei")
# else:
#     print("shuud orj bolno")
# task 21
# a, b, = map(int,input("dun. bolon irtsee oruul ").split())
# c= 60
# if a >= c and b>=80:
#     print("pass")
# else:
#     print("fail")
#  task 22
# password1= input('enter your password  :')
# if password1 == "python123":
#     password2 = input("enter again :")
#     if password2 == "python123":
#         print("logged in")
#     else:
#         print("password incorrect")
# else:
#     print("password is incorrect")
# task 23
# a, b, c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split())
# if a < b < c:
#     print(b)
# if a < c < b:
#      print(c)
# if b < a < c:
#     print(a)

# task 24
# onoo, irts = map(int, input("dun. bolon irtsee oruul ").split())
# if onoo >= 90 and irts >= 90:
#     print("Excellent")
# elif onoo >= 70 and irts >= 80:
#     print("Good")
# else:
#     print("Need Improvement")
# task 25
# udur = input("ajiliin uduruu bich ")
# if udur == "6" or udur == "7":
#     print("amraltiin odor")
# else:
#     print("ajiliin udur")    

# dun =  int(input("udruu oruul "))
# if dun == 1:
#     print("monday ")
# elif dun ==2:
#     print("tuesday")
# elif dun ==3:
#     print("wednesday")
# elif dun ==4:
#     print("thursday")
# elif dun ==5:
#     print("friday")
# elif dun ==6:
#     print("saturday weekend")
# elif dun ==7:
#     print("sunday weekend")
# else:
#     print("tiim odr gej bhkuu")

# task 26
# n = int(input("too oruul: "))
# if n > 100 and n % 2 == 0:
#     print("Large Even")
# elif n > 100:
#     print("Large")
# elif 0 <= n <= 100:
#     print("Medium")
# else:
#     print("Negative")

# task 27
# p, a = map(int, input("uniin dun blon nasaa bichne uu: ").split())
# if a < 18:
#     discount = 0.20 
# elif a > 60:
#     discount = 0.30  
# else:
#     discount = 0.00  
# niit = int(p * (1 - discount))
# print(niit)
# task 28
# a, b, c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split())
# if a+b>c and a+c>b and b+c>a:
#     print("yes")
# else:
#     print("no")
# task 29
# age = int(input("nasaa oruul "))
# admin = input("admin uu? (yes/no): ")
# password = input("passwordaa oruul: ")  
# password =int(password)  
# if age < 18:
#     print("yee suga ")
# elif password == 1234:
#     print("marttsan uu")
# else:
#     if admin == "yes":
#         print("admin")
#     else:
#         print("admin l orno")
# task 30
# balance, money = map(int,input("dasnii uldegdel bolon avah gej bgaa too hemjeegee bichne uu ").split())
# if balance <= 0:
#     print("invalid")
# elif money > balance:
#     print("inf balance")
# elif money % 1000 != 0:
#     print("inv amount")
# else:
#     print("remaing", balance - money)