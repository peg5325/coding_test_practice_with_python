# 백준 1407번 - 2로 몇 번 나누어질까
# https://www.acmicpc.net/problem/1407

# 완전탐색
import sys

input = sys.stdin.readline

# a, b = map(int, input().split())
# res = 0

# for i in range(a, b+1):
#     if i % 2 != 0:
#         res += 1
#     else:
#         tmp = 0
#         while i % 2 == 0:
#             i = i/2
#             tmp += 1
#         res += 2**tmp

# print(res)


# 최적화
a, b = map(int, input().split())

a -= 1
tmp_a = a

for i in range(1, 99):
    tmp_a += (a // (2**i)) * ((2**i) - (2 ** (i - 1)))

tmp_b = b

for i in range(1, 99):
    tmp_b += (b // (2**i)) * ((2**i) - (2 ** (i - 1)))

print(tmp_b - tmp_a)
