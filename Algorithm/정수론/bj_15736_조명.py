# 백준 15736번 - 청기 백기
# https://www.acmicpc.net/problem/15736

import sys

input = sys.stdin.readline

# n = int(input())
# res = 0

# for i in range(1, n+1):
#     if (i * i) >= n:
#         break
#     else:
#         res += 1

# print(res)


# 최적화
n = int(input())

answer = int(n**0.5)

print(answer)
