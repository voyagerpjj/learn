import multiprocessing as mp


# 冒泡排序
def sort_bubble(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# 桶排序
def sort_bucket(data):
    # 创建桶列表，每个桶用一个列表表示
    num_buckets = len(data) / 100
    buckets = [[] for _ in range(int(num_buckets))]

    # 将待排序数组中的元素分配到对应的桶中
    for num in data:
        bucket_index = int(num % 100)
        buckets[bucket_index].append(num)
    # 对每个非空桶中的元素进行排序
    for bucket in buckets:
        bucket.sort()

    # 合并所有桶中的元素
    sorted_data = []
    for bucket in buckets:
        sorted_data.extend(bucket)

    return sorted_data

# 选择排序
def sort_selection(data):
    data_count = len(data)
    for i in range(data_count):
        min_index = i
        for j in range(i + 1, data_count):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


# 归并排序
def sort_merge(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = sort_merge(data[:mid])
    right = sort_merge(data[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 插入排序
def sort_insertion(data):
    n = len(data)
    progress_update_count = 0
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


# 插入排序函数
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


# 处理每个块的排序
def process_chunk(data_chunk):
    return insertion_sort(data_chunk)


# 多进程排序函数
def parallel_insertion_sort(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]

    with mp.Pool(processes=num_chunks) as pool:
        sorted_chunks = pool.map(process_chunk, chunks)

    sorted_data = merge_sorted_chunks(sorted_chunks)
    return sorted_data


# 合并排序块
def merge_sorted_chunks(chunks):
    result = []
    for chunk in chunks:
        result.extend(chunk)
    return insertion_sort(result)


# 希尔排序
def sort_shell(data):
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2
    return data


# 堆排序
def sort_heap(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    return data


# heapify
def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and data[l] > data[largest]:
        largest = l
    if r < n and data[r] > data[largest]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


# 快速排序
def sort_quick(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return sort_quick(left) + middle + sort_quick(right)


# 基数排序
def sort_radix_one(data, exp):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = data[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = data[i] // exp
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(data)):
        data[i] = output[i]


def sort_radix(data):
    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        sort_radix_one(data, exp)
        exp *= 10
    return data