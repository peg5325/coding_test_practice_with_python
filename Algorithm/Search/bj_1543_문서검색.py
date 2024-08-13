# 백준 1543번 - 문서 검색
# https://www.acmicpc.net/problem/1543

from sys import stdin

input = stdin.readline

document = input().strip()
word = input().strip()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1

print(result)