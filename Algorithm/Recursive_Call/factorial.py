# 재귀용법 (Recursive Call)
# 재귀 호출은 스택의 전형적인 예시
# 추가적으로 Python 에서 재귀 함수는 깊이가 (한번에 호출 되는) 1,000회 이하가 되어야 함.

# 예제로 Factorial 사용

# 일반적인 형태 1
def factorial_1(n):
    if n > 1:
        return n * factorial_1(n-1)
    else:
        return n

# 일반적인 형태 2
def factorial_2(n):
    if n <= 1:
        return n
    return_value = n * factorial_2(n-1)
    return return_value

#결과 확인하기
print(factorial_1(5) == (5*4*3*2*1))
print(factorial_2(5) == (5*4*3*2*1))

