# 백준 2720번 - 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720

import sys

input = sys.stdin.readline
t = int(input())
m = [int(input()) for _ in range(t)]

for i in range(t):
    Q, q = [m[i] // 25, m[i] % 25]
    D, d = [q // 10, q % 10]
    N, n = [d // 5, d % 5]
    P = n // 1

    print(Q, D, N, P)