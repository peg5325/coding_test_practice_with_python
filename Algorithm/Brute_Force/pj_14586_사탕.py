# 백준 14568번 사탕
# https://www.acmicpc.net/problem/14568

import sys

input = sys.stdin.readline

candy = int(input())

count = 0

for A in range(0, candy + 1):
    for B in range(0, candy + 1):
        for C in range(0, candy + 1):
            if A + B + C == candy:
                if A >= B + 2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            count += 1

print(count)
