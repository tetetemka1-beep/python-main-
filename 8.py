# task1
# s = input()
# words = s.split()
# print(len(words))
# task 2
# words = input().split()
# longest = max(words, key=len)
# print(longest)
# task 3
# s = input().lower()
# vowels = "аэиоуөү"
# count = 0
# for ch in s:
#     if ch in vowels:
#         count += 1
# print(count)
# task 4
# s = input()
# word = input()
# print(s.split().count(word))
# task 5
# words = input().split()
# words.sort()
# print(" ".join(words))
# task 6
# words = input().split()
# for word in words:
#     if word == word[::-1]:
#         print(word, end=" ")
# task 7
# names = input().split()
# for name in names:
#     print(name, len(name))
# task 8
# s = input()
# most = max(s, key=s.count)
# print(most, s.count(most))
# task 9
# words = input().split()
# result = []
# for word in words:
#     if word not in result:
#         result.append(word)
# print(" ".join(result))
# task 10
# data = input().split()
# names = []
# scores = []
# for item in data:
#     name, score = item.split(":")
#     names.append(name)
#     scores.append(int(score))
# highest = max(scores)
# for i in range(len(scores)):
#     if scores[i] == highest:
#         print(names[i], scores[i])
