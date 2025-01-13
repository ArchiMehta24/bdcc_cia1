import random
import time
from multiprocessing import Pool

def generate_list(size):
    return [random.randint(1, 10000) for _ in range(size)]

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge_sort_parallel(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    with Pool(2) as pool:
        left, right = pool.map(merge_sort, [arr[:mid], arr[mid:]])
    return merge(left, right)

if __name__ == "__main__":
    size = 50000
    data = generate_list(size)
    start_time = time.time()
    sorted_data = merge_sort_parallel(data)
    end_time = time.time()
    print(f"Time taken (Multiprocessing): {end_time - start_time:.2f} seconds")
