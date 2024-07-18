from src.题目1.题目1_1 import read_data


if __name__ == "__main__":
    data = read_data("E:\python\小学期\数据文件2024.txt")
    last_i = 0
    last_last_i = 0
    num = []
    for i in data:
        if i - last_i == last_i - last_last_i:
            num_1 = [last_last_i, last_i, i]
            n = {"place": data.index(last_last_i), "data": num_1}
            num.append(n)
        last_last_i = last_i
        last_i = i
    print(num)
    with open("E:\python\小学期\data/题目1.7.txt", "w", encoding="utf-8") as f:
        str1 = "一共有 " + str(len(num)) + " 个等差数列" + "\n"
        str2 = "分别是"
        str3 = "\n"
        for i in range(len(num)):
            str3 += "位置是 " + str(num[i]["place"]) + " 数据是 " + str(num[i]["data"]) + "\n"
        f.write(str1 + str2 + str3)


