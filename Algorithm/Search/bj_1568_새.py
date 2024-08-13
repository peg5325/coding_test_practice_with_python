# 백준 1568번 새
# https://www.acmicpc.net/problem/1568

from sys import stdin

input = stdin.readline

n = int(input())
k = 1
count = 0

while n != 0:
    if k > n:
        k = 1

    n -= k
    k += 1
    count += 1

print(count)