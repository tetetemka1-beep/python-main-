# task 1
# nemelt 10 dasgal
# jil = int(input("jilee oruulna uu "))
# if jil % 4 == 0 and jil % 100 > 0:
#     print("yes")
# else:
#     print("no")
# task 2
# a,b,c, = map(int,input("gurvaljinii 3 tal oruulna uu ").split())
# if a < 0 or b < 0 or c < 0:
#     print("gurvaljin bolohkuu")
# elif a==b and b==c and c==a:
#         print("adil talt gurvaljin")
# elif a == b or a == c or b == c:
#         print("2 taliin gurvaljin")
# else: 
#     print("gurvaljin bolno")
# task 4
# username= input('username :')
# if username == "tete":
#     password = input("password :")
#     if password == "1234":
#         print("logged in")
#     else:
#         print("bloked")
# else:
#     print("welcome")
# task 7
# day, month, year=map(int,input("odr sar jil oruul  ").split())
# if month < 1 or month > 12 or day < 1:
#     print("INVALID")
# elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     if day <=31:
#         print("valid")
#     else:
#         print("invalid")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     if day <=30:
#         print("valid")
#     else:
#         print("invalid")
# elif month == 2:
#     if year % 400 == 0 and day <=29 or year % 400 != 0 and day <=28 :
#         print("valid")
#     else :
#         print("invalid")
# else:
#     print("invalid")
# task 9
# dun, irts, zorchil = map(int, input("dun irts zorchil ").split())
# if dun >= 90 and irts >= 95 and zorchil == 0:
#     print("FULL")
# elif dun >= 80 and irts >= 90 and zorchil <= 1:
#     print("HALF")
# else:
#     print("NONE")
# task 10
# player1 =  input("player1 : ")
# player2 = input("player2: ")
# if player1 == player2:
#     print("draw")
# elif (player1 == "r" and player2 == "s") or (player1 == "s" and player2 == "p") or (player1 == "p" and player2 == "r"):
#     print("player1 win")
# else:
#     print("player 2 win ")
# task 5
# x1, x2, y1, y2 = map(int, input().split())
# x , y = map(int , input().split())
# if x1 <= x <= x2 and y1 <= y <= y2:
#     print("INSIDE")
# else:
#     print("OUTSIDE")
# task6
# a1, a2, b1, b2 = map(int, input().split())
# a , b = map(int , input().split())
# if a1 <= a <= a2 and b1 <= b <= b2:
#     print("YES")
# else:
#     print("NO")
# task 8
# r , s = map(int,input("sss: ").split())
# if (r <1 or r > 8) or (s < 1 or s > 8):
#     print("invalid")
# elif (r + s) % 2 == 0 :
#     print("black")
# else : 
#     print("white")