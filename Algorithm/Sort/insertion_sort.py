# 삽입정렬
# 두 번째 인덱스부터 시작
# 선택한 값과 앞의 인덱스의 값을 비교하기 시작, 맨 앞에 도착하거나 선택한 값보다 작은 값이 나올 때까지 비교

# 시간 복잡도 : O(n^2) --> 이중 반복문으로 최악의 경우

import random


def insertion_sort(data):
    n = len(data)
    for num in range(n - 1):
        for i in range(num + 1, 0, -1):
            if data[i] < data[i - 1]:
                data[i - 1], data[i] = data[i], data[i - 1]
            else:
                break

    return data


dataList = random.sample(range(1, 45), 7)
print(f"정렬 전 : {dataList}")
print(f"정렬 후 : {insertion_sort(dataList)}")
