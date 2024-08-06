# 백준 2436번 - 공약수
# https://www.acmicpc.net/problem/2436

import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())

print(math.gcd(a, b), math.lcm(a, b))

