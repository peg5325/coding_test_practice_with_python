# 1부터 num까지 곱연산 구하기
#
# # 반복문으로 코드 작성
# # def multiple(num):
# #     result = 1
# #     for i in range(1, num + 1):
# #         result *= i
# #
# #     return result
#
# # 재귀 함수로 코드 작성
# def multiple(num):
#     if num <= 1:
#         return num
#     return num * multiple(num-1)
#
# print(multiple(5))

# ------------------------------------------------------------------
# 숫자가 들어 있는 리스트가 주어졌을때, 리스트의 합을 리턴하는 함수를 구하시오

# import random
#
# data = random.sample(range(1, 100), 10)
# print(data)
# def sum_list(data):
#     if len(data) <= 1:
#         return data[0]
#     return data[0] + sum_list(data[1:])
#
# print(sum_list(data))

# ------------------------------------------------------------------
# 회문(Pailndrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드시오.

# def palindrome(word):
#     if len(word) <= 1:
#         return True
#
#     print(f"현재 비교 대상 : {word[0]}, {word[-1]}")
#     if word[0] == word[-1]:
#         return palindrome(word[1:-1])
#     else:
#         return False
#
# import sys
#
# input = sys.stdin.readline
#
# word = input().strip()
# print(palindrome(word))


# ------------------------------------------------------------------
# 정수 n에 대해
# n이 홀수이면 3 * n + 1
# n이 짝수이면 n / 2
# 이렇게 계속 진행해서 n이 결국 1이 될 때까지 위의 과정을 반복합니다.

# def calc(n):
#     print(n)
#
#     if n == 1:
#         return n
#
#     if n % 2 == 0:
#         return calc(int(n / 2))
#     else:
#         return calc(3 * n + 1)
#
# print(calc(3))

# ------------------------------------------------------------------
# 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로만 나타낼 수 있는 방법을 구하시오.

# def func(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#
#     return func(n - 1) + func(n - 2) + func(n - 3)
#
# print(func(10))

# 백준 9095번

# import sys
#
# input = sys.stdin.readline
#
# def func(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#
#     return func(n-1) + func(n-2) + func(n-3)
#
# tc = int(input())
#
# for _ in range(tc):
#     num = int(input())
#     print(func(num))
