# 백준 1236번 - 성 지키기
# https://www.acmicpc.net/problem/1236

# from sys import stdin
#
# input = stdin.readline
#
# N, M = map(int, input().split())
# matrix = [list(input().strip()) for _ in range(N)]
#
# result = 0
#
# for row in range(M):
#     if 'X' not in matrix[row]:
#         result += 1
#
# for col in range(N):
#     t = True
#
#     for row in range(M):
#         if matrix[row][col] == 'X':
#             print("찾았다 요놈")
#             t = False
#             break
#
#     if t:
#         result += 1
#
# print(result)


# --------------------------------
# refactoring

n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input().strip())

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

col_count = 0
for i in range(n):
    if col[i] == 0:
        col_count += 1

print(max(row_count, col_count))