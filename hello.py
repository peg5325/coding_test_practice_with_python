# def sum_many(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(sum_many(1, 2, 3, 4, 5, 8))

# a = 1000
# print(a)

# a = -7
# print(a)

# a = int(1e9)
# print(a)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)

# n = 10
# a = [0] * n
# print(a)

# print(a[3])
# print(a[1:4])

# a = [i+1 for i in range(10)]
# print(a)

# a = [i for i in range(20) if i % 2 == 1]
# print(a)

# n = 4
# m = 3
# a = [[0] * m for _ in range(n)]
# print(a)

# a = [1, 4, 3]

# a.append(2)
# print("append: ", a)

# a.sort()
# print("sort: ", a)

# a.sort(reverse=True)
# print("dsort: ", a)

# a = [1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5, 1}

# result = [i for i in a if i not in remove_set]
# print(result)

# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banan'
# data['코코넛'] = 'Coconut'

# print(data)

# n = int(input())

# data = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

# answer = 8
# print(f"정답은 {answer}입니다.")

# array = [
#     ('홍길동', 50), 
#     ('이순신', 32),
#     ('아무개', 67)
# ]


# def my_key(x):
#     return x[1]


# print(sorted(array, key=my_key))
# print(sorted(array, key=lambda x: x[1]))




# from itertools import permutations
# from itertools import combinations

# data = ['A', 'B', 'C']

# result = list(permutations(data, 3))
# result_comb = list(combinations(data, 2))

# print(result)
# print(result_comb)




# import math


# def lcm(a, b):
#     return a * b // math.gcd(a, b)


# a = 21
# b = 14

# print(math.gcd(21, 14)) 
# print(lcm(21, 14))



# import sys
# import heapq
# input = sys.stdin.readline


# def heapsort(iterable):
#     h = []
#     result = []

#     #모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h, value)
        
#     #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result


# n = int(input())
# arr = []

# for i in range(n):
#     arr.append(int(input()))

# res = heapsort(arr)

# for i in range(n):
#     print(res[i])


