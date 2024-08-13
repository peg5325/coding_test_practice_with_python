# 백준 1302번 - 베스트셀러
# https://www.acmicpc.net/problem/1302

# from sys import stdin
#
# input = stdin.readline
#
# N = int(input())
# books = [input().strip() for _ in range(N)]
#
# count = 0
# max_count = 0
# best_index = 0
#
# sorted(books)
#
# for i in range(N-2):
#     if books[i] == books[i+1]:
#         count += 1
#     elif books[i] != books[i+1]:
#         if max_count == 0:
#             max_count = count
#
#         if count > max_count:
#             max_count = count
#             best_index = i
#
#
#     count = 0
#
#     for j in range(N-1):
#         if i != 0 and books[i] == books[best_index]:
#             continue
#         elif books[i] == books[j]:
#             count += 1
#
#     if count > max_count:
#         max_count = count
#         best_index = i
#
# print(books[best_index])

# ---------------------------------
# refactoring

n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

print(books)

target = max(books.values())
print(target)
array = []

for book, number in books.items():
    if number == target:
        array.append(book)

print(array)

print(sorted(array)[0])


