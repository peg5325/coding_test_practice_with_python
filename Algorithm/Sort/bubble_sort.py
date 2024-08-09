# 버블정렬
# 제일 처음 접하는 정렬 알고리즘
# 두 숫자를 비교, 큰 숫자를 오른쪽으로 스왑하며 정렬된다.
# 그 모습이 마치 거품이 올라오는 모습 같아 버블 정렬이라 불리게 됨

# 시간복잡도 : O(n^2) --> 이중 반복문이므로 최악의 경우

import random


def bubble_sort(data):
    swap = 0
    for num in range(len(data) - 1):
        for index in range(len(data) - num - 1):
            if data[index] > data[index + 1]:
                # temp = data[index]
                # data[index] = data[index + 1]
                # data[index + 1] = temp

                # 파이썬은 이게 되네 ..
                data[index], data[index + 1] = data[index + 1], data[index]

                swap += 1

        if swap == 0:
            print("already sorted")                        
            break

    return data


dataList = random.sample(range(1, 46), 7)

print(f"정렬 전 : {dataList}")
print(f"정렬 후 : {bubble_sort(dataList)}")




