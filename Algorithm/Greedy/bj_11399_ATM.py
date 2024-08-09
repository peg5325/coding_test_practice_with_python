# 백준 11399번 ATM
# https://www.acmicpc.net/problem/11399

n = int(input())
time = sorted(list(map(int, input().split())))
result = 0
addTime = 0

# time.sort()

for i in range(n):
    # addTime += time[i]
    # result += addTime
    result += sum(time[0 : i + 1])

print(result)