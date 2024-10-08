# 선택정렬

import random
import time


def selection_sort(data):
    n = len(data)

    for stand in range(n - 1):
        lowest = stand

        for index in range(stand + 1, n):
            if data[lowest] > data[index]:
                lowest = index

        data[lowest], data[stand] = data[stand], data[lowest]
        # print(f"현재 상황 : {stand}번째, {data}")

    return data


# dataList = random.sample(range(1, 46), 7)
dataList = random.sample(range(100_000), 10_000)

print(f"정렬 전 : {dataList}")
start = time.time()
print(f"정렬 후 : {selection_sort(dataList)}")
end = time.time()
print(f"{end - start : .5f} sec")
