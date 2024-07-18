from src.题目1.题目1_1 import read_data


if __name__ == "__main__":
    data = read_data("E:\python\小学期\数据文件2024.txt")
    last_i = 0
    num = []
    for i in data:
        if abs(i - last_i) == 2:
            num_1 = [last_i, i]
            num.append(num_1)
        last_i = i
    print(num)
    with open("E:\python\小学期\data/题目1.6.txt", "w", encoding="utf-8") as f:
        str1 = "一共有 " + str(len(num)) + " 个二元数组" + "\n"
        str2 = "分别是"
        str3 = "\n"
        for i in range(len(num)):
            str3 += str(num[i]) + "\n"
        f.write(str1 + str2 + str3)


