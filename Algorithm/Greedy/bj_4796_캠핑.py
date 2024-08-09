# 백준 4796번 - 캠핑
# https://www.acmicpc.net/problem/4796

import sys

input = sys.stdin.readline
count = 0

while True:
    l, p, v = map(int, input().split())
    result = 0

    if l == p == v == 0:
        break

    count += 1

    result = (v // p) * l
    result += min((v % p), l)

    # if l < v - (p * (v // p)):
    #     result += l
    # else:
    #     result += v % p

    print(f"Case {count}: {result}")
