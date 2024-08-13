# 퀵 정렬 (Quick sort)

# 정렬 알고리즘의 꽃!
# 기준점(pivot 이라고 부름)을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right) 으로 모으는 함수를 작성함
# 각 왼쪽(left), 오른쪽(right)은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
# 함수는 왼쪽(left) + 기준점(pivot) + 오른쪽(right) 을 리턴함

def qsort(data):
    if len(data) <= 1:
        return data

    # left, right = list(), list()
    pivot = data[0]

    # for i in range(1, len(data)):
    #     if data[i] < pivot:
    #         left.append(data[i])
    #     elif data[i] > pivot:
    #         right.append(data[i])

    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]

    return qsort(left) + [pivot] + qsort(right)


import random
import time

# data_list = random.sample(range(1, 100), 10)
data_list = random.sample(range(100_000), 10_000)

print(f"정렬 전 : {data_list}")
start = time.time()
print(qsort(data_list))
end = time.time()
print(f"{end - start: .5f} sec")
