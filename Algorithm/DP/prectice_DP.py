# 동적 계획법 (Dynamic Programming)

# 동적계획법 (DP 라고 많이 부름)
#   > 입력 크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 보다 큰 크기의 부분 문제를 해결, 최종적으로 전체 문제를 해결하는 알고리즘
#   > 상향식 접근법으로, 가장 최하위 해답을 구한 후, 이를 저장하고, 해당 결과값을 이용해서 상위 문제를 풀어가는 방식
#   > Memoization 기법을 사용함
#       - Memoization (메모이제이션) 이란: 프로그램 실행 시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술
#   > 문제를 잘게 쪼갤 때, 부분 문제는 중복되어, 재활용됨
#       - 예: 피보나치 수열

# 1. Recursive Call 을 이용한 피보나치 수열

# def fibonacci(n):
#     if n <= 1:
#         return n
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# num = int(input())
#
# for i in range(num):
#     print(f"Fibonacci {i} -> {fibonacci(i)}")


# 2. DP 를 활용한 피보나치 수열
def fibo_dp(n):
    # Memorization 을 활용하기 위한 공간 생성
    cache = [0 for index in range(n+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, n+1):
        cache[index] = cache[index-1] + cache[index-2]

    return cache[n]

print(fibo_dp(10))
