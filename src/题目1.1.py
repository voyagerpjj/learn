import time
from rich.progress import Progress
from src import 排序算法


# 读取数据
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        data_list = [item.strip() for item in data.split(',')]
        data_list = [item.strip('\n') for item in data_list]
        data_list = [int(x) for x in data_list]
        print(f"读取数据完成，共{len(data_list)}条数据")
        return data_list


# 处理数据
def process_data(data, mode):
    start_time = time.time()
    end_sort_time = 0
    with Progress() as progress:
        task = progress.add_task("排序中...", total=len(data))
        if mode == 1:
            排序算法.sort_bubble(data, task, progress)
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
        end_sort_time = time.time()
    print(f"排序完成，耗时：{(end_sort_time - start_time)}s")
    write_data(data, mode)
    end_time = time.time()
    print(f"处理完成，耗时：{(end_time - start_time)}s")


# 写入处理结果
def write_data(data, mode):
    if mode == 1:
        with open('处理结果1（冒泡）.txt', 'w') as file:
            file.write(', '.join(str(data)))
    elif mode == 2:
        with open('处理结果2（选择）.txt', 'w') as file:
            file.write(', '.join(data))
    elif mode == 3:
        with open('处理结果3（归并）.txt', 'w') as file:
            file.write(', '.join(data))
    elif mode == 4:
        with open('处理结果4（插入）.txt', 'w') as file:
            file.write(', '.join(data))
    elif mode == 5:
        with open('处理结果5（希尔）.txt', 'w') as file:
            file.write(', '.join(data))
    elif mode == 6:
        with open('处理结果6（堆）.txt', 'w') as file:
            file.write(', '.join(data))
    elif mode == 7:
        with open('处理结果7（快速）.txt', 'w') as file:
            file.write(', '.join(str(data) for data in data))
    elif mode == 8:
        with open('处理结果8（桶）.txt', 'w') as file:
            file.write(', '.join(data))
    print("处理结果已写入文件")


# 主运行函数
def main():
    data = read_data("数据文件2024.txt")
    data = read_data("处理结果7（快速）.txt")
    print(f"打印示例数据:{data[0::50]}")
    last_data = 0
    count = 0
    for i in range(2000):
        if int(data[i]) > last_data:
            print(f"逆序对：{last_data} {int(data[i])} {i}")
            count += 1
        last_data = int(data[i])
    print(f"逆序对数:{count}")
    # mode = int(input("请输入排序方式：(1.冒泡排序 2.选择排序"
    #                  "3.归并排序 4.插入排序 5.希尔排序 6.堆排序"
    #                  "7.快速排序 8.桶排序 9.全部运行)"))
    # process_data(data, mode)


if __name__ == "__main__":
    main()
