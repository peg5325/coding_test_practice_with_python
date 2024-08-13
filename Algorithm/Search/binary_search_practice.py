# 이진 탐색 (Binary Search)

# 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법
def binary_search(data_list, find_data):
    n = len(data_list)

    if n == 1 and find_data == data_list[0]:
        return True
    elif n == 1 and find_data != data_list[0]:
        return False
    elif n == 0:
        return False

    mid = int(n / 2)

    if find_data == data_list[mid]:
        return True
    else:
        if find_data > data_list[mid]:
            return binary_search(data_list[mid+1:], find_data)
        else:
            return binary_search(data_list[:mid], find_data)


import random

data = random.sample(range(100), 10)
data.sort()
print(data)
print(binary_search(data, 25))
