import time
from rich.progress import Progress
from src import 排序算法
from src import 排序算法2
from concurrent.futures import ProcessPoolExecutor


# 读取数据
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        data_list = [item.strip() for item in data.split(',')]
        data_list = [int(x) for x in data_list]
        # for x in data_list:
        #     print(x, end=' ')
        print(f"读取数据完成，共{len(data_list)}条数据")
        return data_list


# 处理数据
def process_data(data, mode, is_progress):
    start_time = time.time()
    end_sort_time = 0
    if is_progress:
        with Progress() as progress:
            task = progress.add_task(f"{sort_name(mode)}排序中...", total=len(data))
            print(f"开始{sort_name(mode)}排序")
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
            end_sort_time = time.time()
    else:
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
    print(f"{sort_name(mode)}排序完成，耗时：{(end_sort_time - start_time)}s")
    write_data(data, mode)
    end_time = time.time()
    print(f"{sort_name(mode)}处理完成，耗时：{(end_time - start_time)}s")


# 写入处理结果
def write_data(data, mode):
    if mode == 1:
        with open('data\处理结果1（基数）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 2:
        with open('data\处理结果2（选择）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 3:
        with open('data\处理结果3（归并）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 4:
        with open('data\处理结果4（插入）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 5:
        with open('data\处理结果5（希尔）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 6:
        with open('data\处理结果6（堆）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 7:
        with open('data\处理结果7（快速）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 8:
        with open('data\处理结果8（桶）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    print(f"处理结果{sort_name(mode)}已写入文件")


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


def sort_name(mode):
    if mode == 1:
        return "1（基数）"
    elif mode == 2:
        return "2（选择）"
    elif mode == 3:
        return "3（归并）"
    elif mode == 4:
        return "4（插入）"
    elif mode == 5:
        return "5（希尔）"
    elif mode == 6:
        return "6（堆）"
    elif mode == 7:
        return "7（快速）"
    elif mode == 8:
        return "8（桶）"
