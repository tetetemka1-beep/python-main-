# def solve(t):
#     days = ["Даваа", "Мягмар", "Лхагва", "Пүрэв", "Баасан", "Бямба", "Ням"]
#     warm = 0 
#     cold= 0 
#     total = 0 
#     streak = longest 
#     below = 0 
#     change = 0
#     change_days = 1
#     start = best = 0
#     for i in range(7):
#         total += t[i]
#     if t[i]>t[warm]:
#         i = warm 
#     if t[i]<t[cold]:
#         i = cold
#     if t[i]<0:
#         below +=1 
#         if streak == 0:
#             start = i
#             streak += 1
#         if streak > longest:
#             longest = streak
#             best = start
#     else:
#         streak = 0 
#     if i > 0:
#         d = t[i]-t[i-1]
#         if d < 0:
#             d = - d
#         if d > change:
#             change = d
#             change_day = i
#     avg = total / 7
# print()