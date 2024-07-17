import time
from rich.progress import Progress
from src import 排序算法
from src import 排序算法2
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp

mode_list = {1: "基数", 2: "选择", 3: "归并", 4: "插入", 5: "希尔", 6: "堆", 7: "快速", 8: "桶"}


# 读取数据
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        data_list = [item.strip() for item in data.split(',')]
        data_list = [int(x) for x in data_list]
        for x in data_list:
            if x < 0:
                print(x, end=' ')
        print(f"读取数据完成，共{len(data_list)}条数据")
        return data_list


# 处理数据
def process_data(data, mode, is_progress):
    start_time = time.time()
    if is_progress:
        with Progress() as progress:
            task = progress.add_task(f"{mode_list[mode]}排序中...", total=len(data))
            print(f"开始{mode_list[mode]}排序")
            if mode == 1:
                排序算法.sort_radix(data, task, progress)
            elif mode == 2:
                排序算法.sort_selection(data, task, progress)
            elif mode == 3:
                排序算法.sort_merge(data, task, progress)
            elif mode == 4:
                排序算法.sort_insertion(data, task, progress)
            elif mode == 5:
                排序算法.sort_shell(data, task, progress)
            elif mode == 6:
                排序算法.sort_heap(data, task, progress)
            elif mode == 7:
                排序算法.sort_quick(data, task, progress)
            elif mode == 8:
                排序算法.sort_bucket(data, task, progress)
    else:
        print(f"开始{mode_list[mode]}排序")
        if mode == 1:
            排序算法2.sort_radix(data)
        elif mode == 2:
            排序算法2.sort_selection(data)
        elif mode == 3:
            排序算法2.sort_merge(data)
        elif mode == 4:
            排序算法2.sort_insertion(data)
        elif mode == 5:
            排序算法2.sort_shell(data)
        elif mode == 6:
            排序算法2.sort_heap(data)
        elif mode == 7:
            排序算法2.sort_quick(data)
        elif mode == 8:
            排序算法2.sort_bucket(data)
    end_sort_time = time.time()
    print(f"{mode_list[mode]}排序完成，耗时：{(end_sort_time - start_time)}s")
    write_data(data, mode)
    end_time = time.time()
    print(f"{mode_list[mode]}处理完成，耗时：{(end_time - start_time)}s")


# 写入处理结果
def write_data(data, mode):
    with open(f'data\处理结果{mode}（{mode_list[mode]}）排序.txt', 'w') as file:
        file.write(', '.join(str(data) for data in data))
    print(f"处理结果 {mode_list[mode]}排序 已写入文件")


# 主运行函数
def main():
    data = read_data("数据文件2024.txt")
    # data = read_data("处理结果7（快速）.txt")
    # print(f"打印示例数据:{data[0::50]}")
    # last_data = 0
    # count = 0
    # for i in range(2000):
    #     if int(data[i]) > last_data:
    #         print(f"逆序对：{last_data} {int(data[i])} {i}")
    #         count += 1
    #     last_data = int(data[i])
    # print(f"逆序对数:{count}")
    mode = int(input("请输入排序方式：(1.基数排序 2.选择排序"
                     "3.归并排序 4.插入排序 5.希尔排序 6.堆排序"
                     "7.快速排序 8.桶排序 9.全部运行)"))
    if mode == 9:
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(process_data, data.copy(), i, False) for i in range(1, 9)]
            for future in futures:
                future.result()
    else:
        process_data(data, mode, True)


if __name__ == "__main__":
    main()



