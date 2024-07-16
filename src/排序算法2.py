# 冒泡排序
def sort_bubble(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# 桶排序
def sort_bucket(data):
    bucket = []
    slot_num = 1000
    for i in range(slot_num):
        bucket.append([])
    for j in data:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)
    for i in range(slot_num):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            data[k] = bucket[i][j]
            k += 1
    return data


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
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


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


def sort_radix(data, task, progress):
    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        sort_radix(data, exp)
        exp *= 10
    return data