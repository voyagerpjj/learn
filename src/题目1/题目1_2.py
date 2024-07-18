from src.题目1.题目1_1 import read_data


# 主程序
if __name__ == "__main__":
    data = read_data("data/处理结果5（希尔）排序.txt")
    print(len(data))
    strs = []
    with open("data/题目1.2.txt", "w", encoding="utf-8") as f:
        strs.append("数据一共有" + str(len(data)) + "条")
        strs.append("数据第1个是" + str(data[0]))
        strs.append("数据第177个是" + str(data[176]))
        strs.append("数据第189个是" + str(data[188]))
        strs.append("数据第1279个是" + str(data[1278]))
        strs.append("数据第3949个是" + str(data[3948]))
        for i in range(6):
            print(strs[i])
        f.write("\n".join(strs))



