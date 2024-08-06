# 백준 2503번 - 숫자야구
# https://www.acmicpc.net/problem/2503

import sys

input = sys.stdin.readline

n = int(input())

numbers = [list(map(str, input().split())) for _ in range(n)]

answer = 0

for a in range(1, 10):  # 100의 자릿수
    for b in range(1, 10):  # 10의 자릿수
        for c in range(1, 10):  # 1의 자릿수
            counter = 0

            # 조건 : 모든 자리수는 달라야 한다.
            if a == b or b == c or a == c:
                continue

            for array in numbers:
                check = list(array[0])
                strike = int(array[1])
                ball = int(array[2])

                strike_count = 0
                ball_count = 0

                if a == int(check[0]):
                    strike_count += 1
                if b == int(check[1]):
                    strike_count += 1
                if c == int(check[2]):
                    strike_count += 1

                if a == int(check[1]) or a == int(check[2]):
                    ball_count += 1
                if b == int(check[0]) or b == int(check[2]):
                    ball_count += 1
                if c == int(check[0]) or c == int(check[1]):
                    ball_count += 1

                if strike != strike_count:
                    break
                if ball != ball_count:
                    break

                counter += 1

            if counter == n:
                answer += 1

print(answer)
