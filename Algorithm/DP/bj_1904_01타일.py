# 백준 1904번 01 타일
# https://www.acmicpc.net/problem/1904

import sys

input = sys.stdin.readline

dp = [0] * 1_000_001

dp[1] = 1
dp[2] = 2

N = int(input())

for i in range(3, N+1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[N])
