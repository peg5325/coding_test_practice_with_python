# 백준 2304번 - 창고 다각형
# https://www.acmicpc.net/problem/2304

import sys

input = sys.stdin.readline

N = int(input())
poles = [list(map(int, input().split())) for _ in range(N)]

sorted_poles = sorted(poles)

max_h = 0
total = 0

# 최대 높이 찾기
for i in range(N):
    max_h = max(max_h, sorted_poles[i][1])

# 처음부터 가장 높은 지점까지
for i in range(1, N):



# 마지막에서 가장 높은 지점까지 역순
# for i in range(N-1, -1, -1):
#     ----

# total += max_h

# print(total)