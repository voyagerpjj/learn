# 冒泡排序
def sort_bubble(data, task, progress):
    count = 0

    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        count += 1
        progress.update(task, advance=1)
        # if count % 1000 == 0:
        #     print(f"已排序{count}条数据")
    return data


# 选择排序
def sort_selection(data, task, progress):
    data_count = len(data)
    count = 0
    for i in range(data_count):
        min_index = i
        for j in range(i + 1, data_count):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        count += 1
        progress.update(task, advance=1)
        # if count % 100 == 0:
        #     print(f"已排序{count}条数据")
    return data


# 归并排序
def sort_merge(data, task, progress):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    L = data[:mid]  # 截取前半部分
    R = data[mid:]  # 截取后半部分
    sort_merge(L)
    sort_merge(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1
        progress.update(task, advance=1)
    while i < len(L):
        data[k] = L[i]
        i += 1
        k += 1
        progress.update(task, advance=1)
    while j < len(R):
        data[k] = R[j]
        j += 1
        k += 1
        progress.update(task, advance=1)
    return data


# 插入排序
def sort_insertion(data, task, progress):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        progress.update(task, advance=1)
    return data


# 希尔排序
def sort_shell(data, task, progress):
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
        progress.update(task, advance=1)
    return data


# 堆排序
def sort_heap(data, task, progress):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
        progress.update(task, advance=(n / n // 2 - 1))
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
        progress.update(task, advance=(n / n - 1))
    return data


# heapify
def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and data[i] < data[l]:
        largest = l
    if r < n and data[largest] < data[r]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


# 快速排序
def sort_quick(data, task, progress):
    if len(data) <= 1:
        progress.update(task, advance=1)
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    progress.update(task, advance=1)
    return sort_quick(left, task, progress) + middle + sort_quick(right, task, progress)
