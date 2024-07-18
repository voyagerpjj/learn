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


if __name__ == "__main__":
    matrix = [
        [1, 2, -1, -5],
        [2, 3, -1, -11],
        [-2, 0, -3, 22]
    ]

    rref_matrix = to_reduced_row_echelon_form(matrix)
    print(f"阶梯型矩阵：\n{rref_matrix}")
