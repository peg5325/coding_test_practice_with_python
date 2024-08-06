# Brute Force : 완전 탐색
# '근본' 알고리즘

# 백준 1816번 - 비밀번호
# https://www.acmicpc.net/problem/1816

import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())

    for i in range(2, 1_000_001):
        if n % i == 0:
            print("NO")
            break
        elif i == 1_000_000:
            print("YES")
