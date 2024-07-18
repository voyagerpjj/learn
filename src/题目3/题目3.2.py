import numpy as np


def solve_linear_system(equations, constants):
    equations = np.array(equations, dtype=float)
    constants = np.array(constants, dtype=float)
    augmented_matrix = np.hstack([equations, constants.reshape(-1, 1)])

    def to_reduced_row_echelon_form(matrix):
        m, n = matrix.shape
        row = 0  # 当前处理的行

        for col in range(n):
            if row >= m:
                break

            # 找到当前列中绝对值最大的元素
            max_row = np.argmax(np.abs(matrix[row:, col])) + row
            if matrix[max_row, col] == 0:
                continue  # 如果这一列全是0，跳过这一列

            matrix[[row, max_row]] = matrix[[max_row, row]]
            matrix[row] = matrix[row] / matrix[row, col]
            for r in range(m):
                if r != row:
                    matrix[r] -= matrix[r, col] * matrix[row]

            row += 1

        return matrix

    # 将增广矩阵转换为阶梯型矩阵
    rref_matrix = to_reduced_row_echelon_form(augmented_matrix)

    # 计算解
    m, n = equations.shape
    solutions = np.zeros(n)
    for i in range(m):
        pivot_col = np.where(rref_matrix[i, :-1] != 0)[0]
        if len(pivot_col) == 0:
            continue  # 跳过全零行
        pivot_col = pivot_col[0]
        solutions[pivot_col] = rref_matrix[i, -1]

    return solutions


if __name__ == "__main__":

    equations = [
        [2, -1, 3],
        [1, 2, -1],
        [3, -1, -2]
    ]
    constants = [10, 3, -1]

    solutions = solve_linear_system(equations, constants)
    str1 = str(f"原方程为{equations}\n{constants}")
    str2 = str(f"\n方程组的解：\n{solutions}")
    print(str2)
    with open("E:\python\小学期/data/题目3.2.txt", "w", encoding="utf-8") as f:
        f.write(str1 + str2)
