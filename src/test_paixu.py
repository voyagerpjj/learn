import numpy as np
from numba import cuda
import time
from rich.progress import Progress


# 读取数据
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        data_list = [item.strip() for item in data.split(',')]
        data_list = np.array([int(x) for x in data_list], dtype=np.int64)
        print(f"读取数据完成，共{len(data_list)}条数据")
        return data_list

@cuda.jit
def quicksort_kernel(data, left, right):
    stack = cuda.local.array(1024, dtype=np.int32)
    top = -1

    top += 1
    stack[top] = left
    top += 1
    stack[top] = right

    while top >= 0:
        right = stack[top]
        top -= 1
        left = stack[top]
        top -= 1

        i = left
        j = right
        pivot = data[(left + right) // 2]

        while i <= j:
            while data[i] < pivot:
                i += 1
            while data[j] > pivot:
                j -= 1
            if i <= j:
                data[i], data[j] = data[j], data[i]
                i += 1
                j -= 1

        if left < j:
            top += 1
            stack[top] = left
            top += 1
            stack[top] = j
        if i < right:
            top += 1
            stack[top] = i
            top += 1
            stack[top] = right

def quicksort(data):
    n = len(data)
    threads_per_block = 256
    blocks_per_grid = (n + (threads_per_block - 1)) // threads_per_block
    quicksort_kernel[blocks_per_grid, threads_per_block](data, 0, n - 1)

# 处理数据
def process_data(data):
    start_time = time.time()
    with Progress() as progress:
        task = progress.add_task("排序中...", total=1)
        quicksort(data)
        progress.update(task, advance=1)
    end_sort_time = time.time()
    print(f"排序完成，耗时：{(end_sort_time - start_time)}s")
    write_data(data)
    end_time = time.time()
    print(f"处理完成，耗时：{(end_time - start_time)}s")

# 写入处理结果
def write_data(data):
    with open('处理结果（快速GPU）.txt', 'w') as file:
        file.write(', '.join(str(x) for x in data))
    print("处理结果已写入文件")

# 主运行函数
def main():
    data = read_data("数据文件2024.txt")
    process_data(data)

if __name__ == "__main__":
    main()
