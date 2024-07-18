from src.题目1.题目1_1 import read_data


if __name__ == "__main__":
    data = read_data("数据文件2024.txt")
    strs = []
    for i in data:
        if 31415 == i:
            strs.append(data.index(i))
    print(strs)
    with open("data/题目1.3.txt", "w", encoding="utf-8") as f:
        if len(strs) == 0:
            str1 = "没有找到31415"
        else:
            str1 = "包含" + " 在" + str(strs[0]) + "个位置"
        f.write(str1)


