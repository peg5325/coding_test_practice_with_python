# 백준 11726번 2*n 타일링
# https://www.acmicpc.net/problem/11726

import sys

input = sys.stdin.readline

num = int(input())


def tiling(n):
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(tiling(num) % 10007)
