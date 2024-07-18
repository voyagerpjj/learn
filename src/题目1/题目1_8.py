from src.题目1.题目1_1 import read_data
import numpy as np
import multiprocessing as mp


# 计算是否是素数
def is_su(num):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_list = []
    count = 0
    for i in num:
        if is_prime(i):
            prime_list.append(i)
        count += 1
        if count % 1000 == 0:
            print(f"已经计算了{count}个数字")
    return prime_list


# 多进程加速
def parallel_is_su(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]
    print(f"已经启动多进程加速，共有{num_chunks}个进程")
    with mp.Pool(processes=num_chunks) as pool:
        num_list = pool.map(is_su, chunks)

    result = []
    for num in num_list:
        result.extend(num)
    return result


def main():
    data = read_data("数据文件2024.txt")
    num_list = parallel_is_su(data, mp.cpu_count())
    print(num_list)
    print(len(num_list))
    with open("data/题目1.8.txt", "w", encoding="utf-8") as f:
        str1 = "一共有 " + str(len(num_list)) + " 个素数" + "\n"
        str4 = "最大值是" + str(np.max(num_list))
        f.write(str1 + str4)


if __name__ == "__main__":
    main()
