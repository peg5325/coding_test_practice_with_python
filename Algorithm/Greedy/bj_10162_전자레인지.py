# 백준 10162번
# https://www.acmicpc.net/problem/10162

import sys

input = sys.stdin.readline
t = int(input())

if t % 10 != 0:
    print(-1)
else:
    a, t = [t // 300, t % 300]
    b, t = [t // 60, t % 60]
    c = t // 10

    print(a, b, c)
