# 백준 1668번 - 트로피 진열
# https://www.acmicpc.net/problem/1668

def ascending(arr):
    max_height = 0
    count = 0

    for i in range(len(arr)):
        if max_height < arr[i]:
            count += 1
            max_height = arr[i]
    return count


from sys import stdin

input = stdin.readline

n = int(input())
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = int(input())

print(ascending(arr))
arr.reverse()
print(ascending(arr))


