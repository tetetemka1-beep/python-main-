# task 1
# s = input()
# words = s.split()
# unique = list(set(words))
# unique.sort(key=len, reverse=True)
# if len(unique) < 2:
#     print("NO")
# else:
#     print(unique[1])
# task 2
# s = input()
# result = ""
# count = 1
# for i in range(len(s)):
#     if i < len(s) - 1 and s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1
# print(result)
# task 3
# s = input()
# words = s.split()
# result = []
# for word in words:
#     result.append(word[::-1])
# print(" ".join(result))
# task 4
# s = input()
# words = s.split()
# vowels = "aeiou"
# max_count = 0
# answer = ""
# for word in words:
#     count = 0
#     for ch in word.lower():
#         if ch in vowels:
#             count += 1
#     if count > max_count:
#         max_count = count
#         answer = word
# print(answer, max_count)
# task 5
# a = input().lower()
# b = input().lower()
# if sorted(a) == sorted(b):
#     print("YES")
# else:
#     print("NO")
# task 6
# s = input()
# words = s.split()
# for word in words:
#     if words.count(word) > 1 and words.index(word) == words.index(word):
#         if words.index(word) == words.index(word):
#             pass
# result = []
# for word in words:
#     if word not in result:
#         result.append(word)
# for word in result:
#     if words.count(word) > 1:
#         print(word, words.count(word))
# task 7
# s = input()
# s = s.replace(" ", "").lower()
# if s == s[::-1]:
#     print("YES")
# else:
#     print("NO")
# task 8
# s = input()
# words = s.split()
# result = []
# for word in words:
#     for ch in word:
#         if ch.isdigit():
#             result.append(word)
#             break
# if len(result) > 0:
#     print(" ".join(result))
# else:
#     print("NO")
# task 9
# s = input()
# upper = False
# lower = False
# digit = False
# special = False
# for ch in s:
#     if ch.isupper():
#         upper = True
#     if ch.islower():
#         lower = True
#     if ch.isdigit():
#         digit = True
#     if ch in "!@#$":
#         special = True
# if len(s) >= 8 and upper and lower and digit and special and " " not in s:
#     print("STRONG")
# else:
#     print("WEAK")
# task 10
# s = input()
# data = s.split()
# names = []
# scores = []
# for item in data:
#     name, score = item.split(":")
#     names.append(name)
#     scores.append(int(score))
# highest = max(scores)
# average = sum(scores) / len(scores)
# print("Highest:", end=" ")
# for i in range(len(names)):
#     if scores[i] == highest:
#         print(names[i], end=" ")
# print()
# print("Average:", round(average, 1))
# print("Above average:", end=" ")
# for i in range(len(names)):
#     if scores[i] > average:
#         print(names[i], end=" ")
# print()
# print("Failed:", end=" ")
# for i in range(len(names)):
#     if scores[i] < 60:
#         print(names[i], end=" ")
# print()