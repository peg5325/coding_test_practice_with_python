# 백준 1920번 - 수 찾기
# https://www.acmicpc.net/problem/1920


#import sys


# def bs(data_list, find_data):
#     n = len(data_list)
#
#     if n == 1 and find_data == data_list[0]:
#         return 1
#     elif n == 1 and find_data == data_list[0]:
#         return 0
#     elif n == 0:
#         return 0
#
#     mid = int(n / 2)
#
#     if find_data == data_list[mid]:
#         return 1
#     else:
#         if find_data > data_list[mid]:
#             return bs(data_list[mid + 1:], find_data)
#         else:
#             return bs(data_list[:mid], find_data)
#
#
# input = sys.stdin.readline
#
# n = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
#
# m = int(input())
# find_data_list = map(int, input().split())
#
# for item in find_data_list:
#     print(bs(nums, item))


# Refactoring ---------------------------

def bs(find_data, start, end):
    if start > end:
        return 0

    mid = int((start + end) / 2)

    if find_data > n_list[mid]:
        return bs(find_data, mid + 1, end)
    elif find_data < n_list[mid]:
        return bs(find_data, start, mid - 1)
    else:
        return 1


input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = map(int, input().split())

for item in m_list:
    print(bs(item, 0, n - 1))
