# 백준 19532번 연립방정식
# https://www.acmicpc.net/problem/19532

import sys

input = sys.stdin.readline

A, B, C, D, E, F = map(int, input().split())

for i in range(-10000, 10001):
    for j in range(-10000, 10001):
        if (A * i) + (B * j) == C:
            if (D * i) + (E * j) == F:
                print(i, j)
                break
