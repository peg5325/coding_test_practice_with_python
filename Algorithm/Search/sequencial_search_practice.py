# 순차 탐색 (Sequencial Search)

# 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법

def sequencial_search(data_list, find_data):
    for index in range(len(data_list)):
        if find_data == data_list[index]:
            return index

    return -1


from random import *
import time

# rand_data_list = list()
# for num in range(1_000_000):
#     rand_data_list.append(randint(1, 1_000_000))
rand_data_list = sample(range(1, 1_000_000), 100_000)

# print(rand_data_list)
start = time.time()
print(sequencial_search(rand_data_list, 1004))
end = time.time()
print(f"{end - start : .5f} sec")
