import numpy as np


# 函数用于将矩阵转换为阶梯型矩阵
def to_reduced_row_echelon_form(matrix):
    matrix = np.array(matrix, dtype=float)
    m, n = matrix.shape
    row = 0  # 当前处理的行

    for col in range(n):
        if row >= m:
            break

        # 找到当前列中绝对值最大的元素
        max_row = np.argmax(np.abs(matrix[row:, col])) + row
        if matrix[max_row, col] == 0:  # 如果这一列全是0，跳过这一列
            continue

        matrix[[row, max_row]] = matrix[[max_row, row]]
        matrix[row] = matrix[row] / matrix[row, col]

        # 消去其他行的当前列元素
        for r in range(m):
            if r != row:
                matrix[r] -= matrix[r, col] * matrix[row]

        row += 1

    return np.array(matrix, dtype=int)


# 函数用于输入矩阵
def input_matrix():
    rows = int(input("请输入矩阵的行数："))
    cols = int(input("请输入矩阵的列数："))

    matrix = []
    for i in range(rows):
        row = input(f"请输入矩阵第 {i + 1} 行（以空格分隔）：").split()
        matrix.append([float(x) for x in row])

    return matrix


def main():
    is_input = int(input(f"是否输入矩阵？(1是/0否)："))
    if is_input:
        matrix = input_matrix()
    else:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    rref_matrix = to_reduced_row_echelon_form(matrix)
    str1 = str(f"原矩阵为{matrix}\n")
    str2 = str(f"阶梯型矩阵：\n{rref_matrix}")
    print(str1)
    print(str2)
    with open("E:\python\小学期/data/题目3.1.txt", "w", encoding="utf-8") as f:
        f.write(str1 + str2)


if __name__ == "__main__":
    main()
