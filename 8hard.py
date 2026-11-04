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
s = input()
words = s.split()
vowels = "aeiou"
max_count = 0
answer = ""
for word in words:
    count = 0
    for ch in word.lower():
        if ch in vowels:
            count += 1
    if count > max_count:
        max_count = count
        answer = word
print(answer, max_count)