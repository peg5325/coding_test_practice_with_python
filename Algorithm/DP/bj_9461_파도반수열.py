# 백준 9461번 파도반 수열
# https://www.acmicpc.net/problem/9461

import sys

input = sys.stdin.readline

def dp(n):
    list = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for i in range(11, 101):
        list.append(list[i-1] + list[i-5])

    return list[n]

tc = int(input())

for _ in range(tc):
    n = int(input())
    print(dp(n))
