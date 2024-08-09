# 백준 11047번 동전 0
# https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
wallet = [int(input()) for i in range(n)]

wallet.sort(reverse=True)

for i in range(n):
    count += k // wallet[i]
    k %= wallet[i]

print(count)