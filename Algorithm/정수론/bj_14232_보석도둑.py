#백준 14232번 - 보석도둑
# https://www.acmicpc.net/problem/14232

import sys

input = sys.stdin.readline

# 완전 탐색
# n = int(input())
# cnt = 0
# num = []

# for i in range(2, n):
#     if n % i == 0:
#         cnt += 1
#         num.append(i)

# print(cnt)
# print(*num)

# 최적화
n = int(input())
cnt = 0
nums = set()

for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        nums.update([i, n//i])

print(len(nums))
print(*sorted(nums))
