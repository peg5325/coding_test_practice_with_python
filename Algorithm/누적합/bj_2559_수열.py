# 백준 2559번 - 수열
# https://www.acmicpc.net/problem/2559

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

total = []
total.append(sum(arr[:k]))

for i in range(n - k):
    total.append(total[i] - arr[i] + arr[i + k])

print(max(total))


# prefix = [0 for _ in range(n+1)]

# for i in range(n):
#     prefix[i + 1] = prefix[i] + arr[i]

# answer = []
# for j in range(k, n+1):
#     answer.append(prefix[j] - prefix[j-k])

# print(max(answer))
