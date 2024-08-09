# 백준 5585번 - 거스름돈
# https://www.acmicpc.net/problem/5585

import sys

input = sys.stdin.readline
m = 1000 - int(input())
count = 0

changes = [500, 100, 50, 10, 5, 1]

for i in changes:
    count += m // i
    m %= i

print(count)
