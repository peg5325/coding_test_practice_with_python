# 병합 정렬 (Merge Sort)
# 분할 정복이 사용 되었지만, Memorization 기법은 사용할 필요 X
import random


def merge_split(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_split(data[:mid])
    right = merge_split(data[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []

    lp, rp = 0, 0

    # case1 - left, right 둘 다 있을 경우
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            sorted_list.append(left[lp])
            lp += 1
        else:
            sorted_list.append(right[rp])
            rp += 1

    # case2 - left 만 남아있을 때
    while lp < len(left):
        sorted_list.append(left[lp])
        lp += 1

    # case3 - right 만 남아있을 때
    while rp < len(right):
        sorted_list.append(right[rp])
        rp += 1

    return sorted_list


data_list = random.sample(range(1, 100), 7)

print(merge_split(data_list))
