from src.题目1.题目1_1 import read_data


if __name__ == "__main__":
    data = read_data("data/处理结果5（希尔）排序.txt")
    num = [str(i) for i in data if "8" in str(i)]
    print(len(num))
    with open("data/题目1.5.txt", "w", encoding="utf-8") as f:
        str1 = "一共有 " + str(len(num)) + " 条数据中含有8"
        f.write(str1)


