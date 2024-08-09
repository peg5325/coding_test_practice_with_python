# 1번 문제

# n = 1260
# count = 0

# array = [500, 100, 50, 10]

# for coin in array:
#     count += n // coin
#     n %= coin

# print(count)

# ----------------------------------------------------
# 2번 문제

# n, k = map(int, input().split())

# result = 0

# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     target = (n // k) * k
#     result += n - target
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += n - 1
# print(result)

# ---------------------------------------------------
# 3번 문제

# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)

# ---------------------------------------------------
# 4번 문제

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0  # 총 그룹의 수
# count = 0  # 현재 그룹에 포함된 모험가의 수

# for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
#     count += 1  # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
#         result += 1  # 총 그룹의 수 증가시키기
#         count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

# print(result)  # 총 그룹의 수 출력

# ---------------------------------------------------

# t = int(input())
# c = []

# for i in range(t):
#     c.append(int(input()))

# q_count = 0
# d_count = 0
# n_count = 0
# p_count = 0

# for i in range(t):
#     total = c[i]
#     result = []

#     q_count = total // 25
#     # result.append(q_count)
#     print(q_count, end=" ")
#     total -= 25 * q_count

#     d_count = total // 10
#     # result.append(d_count)
#     print(d_count, end=" ")
#     total -= 10 * d_count

#     n_count = total // 5
#     # result.append(n_count)
#     print(n_count, end=" ")
#     total -= 5 * n_count

#     p_count = total // 1
#     # result.append(p_count)
#     print(p_count)
#     total -= 1 * p_count

# import sys

# for _ in range(int(sys.stdin.readline())):
#     m = int(sys.stdin.readline())
#     Q, q = [m // 25, m % 25]
#     D, d = [q // 10, q % 10]
#     N, P = [d // 5, d % 5]
#     print(Q, D, N, P)

# import sys

# input = sys.stdin.readline
# count = int(input())
# data = [sum(map(int, input().split())) for _ in range(count)]

# for x in data:
#     print(x)


# ---------------------------------------------------
# 입출력 연습

# import sys

# input = sys.stdin.readline
# n = int(input())
# # data = [input().strip() for _ in range(n)] # N개의 문자열을 여러줄에 걸쳐 입력받아 이차원 배열에 저장할 경우
# data = [list(map(int, input().split())) for _ in range(n)]

# print(data)
