import random

data_list = random.sample(range(1, 46), 7)

# ---------------------------------------------------
# 버블 정렬 (bubble sort)
# ---------------------------------------------------


def bubble_sort(data):
    sorted_list = data
    n = len(sorted_list)
    swapped = False

    for turn in range(n-1):
        for index in range(n-turn-1):
            if sorted_list[index] > sorted_list[index+1]:
                sorted_list[index], sorted_list[index+1] = sorted_list[index+1], sorted_list[index]
                swapped = True

        if swapped == False:
            break

    return sorted_list

# ---------------------------------------------------
# 선택 정렬 (selection sort)
# ---------------------------------------------------


def selection_sort(data):
    sorted_list = data
    n = len(sorted_list)
    swapped = False

    for turn in range(n):
        min_index = turn
        for index in range(turn+1, n):
            if sorted_list[index] < sorted_list[min_index]:
                min_index = index
                swapped = True

        if swapped == False:
            break

        sorted_list[turn], sorted_list[min_index] = sorted_list[min_index], sorted_list[turn]

    return sorted_list

# ---------------------------------------------------
# 선택 정렬 (insertion sort)
# ---------------------------------------------------


def insertion_sort(data):
    sorted_list = data
    n = len(sorted_list)

    for turn in range(n-1):
        for index in range(turn+1, 0, -1):
            if sorted_list[index] < sorted_list[index - 1]:
                sorted_list[index], sorted_list[index - 1] = sorted_list[index - 1], sorted_list[index]

    return sorted_list

# ---------------------------------------------------
# 퀵 정렬 (quick sort)
# ---------------------------------------------------


def quick_sort(data):
    if len(data) <= 0:
        return data

    pivot = data[0]

    left = [item for item in data if item < pivot]
    right = [item for item in data if item > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# ---------------------------------------------------
# 병합 정렬 (merge sort)
# ---------------------------------------------------


def merge_sort(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) / 2)

    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0

    # left, right 둘 다 있는 경우
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # left 만 있는 경우
    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1

    # right 만 있는 경우
    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list

# ---------------------------------------------------
# 결과 확인
# ---------------------------------------------------


print(f"정렬 전 : {data_list} \n ")

print(f"버블 정렬 : {bubble_sort(data_list)}")
print(f"선택 정렬 : {selection_sort(data_list)}")
print(f"삽입 정렬 : {insertion_sort(data_list)}")
print(f"퀵 정렬 : {quick_sort(data_list)}")
print(f"병합 정렬 : {merge_sort(data_list)}")
