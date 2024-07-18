from src.题目1.题目1_1 import read_data


if __name__ == "__main__":
    data = read_data("data/处理结果5（希尔）排序.txt")
    strs = []
    flag = 0
    max_fu = 0
    min_zheng = 0
    num = 0
    All = 0
    for i in data:
        if i < 0:
            max_fu = i
        if i > 0 and flag == 0:
            min_zheng = i
            flag = 1
        if num % 2 == 0:
            All = i ** 2
        num += 1
    pin_jun = sum(data) / len(data)
    print(max_fu, min_zheng, pin_jun, All)
    with open("data/题目1.4.txt", "w", encoding="utf-8") as f:
        strs.append("最小正整数是 " + str(min_zheng))
        strs.append("最大负整数是 " + str(max_fu))
        strs.append("平均数是 " + str(pin_jun))
        strs.append("所有偶数位置平方和是 " + str(All))
        for i in range(4):
            print(strs[i])
        f.write("\n".join(strs))


