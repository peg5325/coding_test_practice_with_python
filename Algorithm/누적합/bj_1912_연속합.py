# 백준 1912번 - 연속합
# https://www.acmicpc.net/problem/1912

n = int(input())
arr = list(map(int, input().split()))

# anwser = [arr[0]]

# for i in range(n-1):
#     anwser.append(max(anwser[i] + arr[i+1], arr[i+1]))

for i in range(1, n):
    if arr[i-1] > 0:
        arr[i] += arr[i-1]

print(max(arr))
