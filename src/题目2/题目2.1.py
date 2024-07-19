import tkinter as tk
from tkinter import messagebox
import sympy as sp


# 输入分式
def on_calculate():
    try:
        numerator = str(numerator_entry.get())
        denominator = str(denominator_entry.get())
        result, is_gen = partial_fraction(numerator, denominator)
        if is_gen:
            result = '\n'.join(map(str, result))
            result_label.config(text=f"部分分式为: {result}")
        else:
            result_label.config(text=f"分母无法因式分解")
    except Exception as e:
        messagebox.showerror("错误", f"出现错误: {e}")


def partial_fraction(numerator, denominator):
    result = []
    x, y = sp.symbols('x y')
    numerator = sp.sympify(numerator)
    denominator = sp.sympify(denominator)
    roots = sp.roots(denominator, x)
    print(roots)
    solution_denominator = []
    for root, multiplicity in roots.items():
        solution_denominator.extend([root] * multiplicity)
    # 获取分子和分母的最大次数
    numerator_degree = sp.Poly(numerator, x).degree()
    denominator_degree = sp.Poly(denominator, x).degree()
    print(f"分子是: {numerator}")
    print(f"分母是: {denominator}")
    print(f"分母的解（包括重复的根）是: {solution_denominator}")
    # 若分母不能被因式分解
    if len(solution_denominator) == 0:
        print("分母没有根")
        result.append(numerator / denominator)
        return result, False
    # 如果分子最高幂次数大于分母最高幂次数
    if numerator_degree >= denominator_degree:
        # 进行多项式长除法
        quotient, remainder = sp.div(numerator, denominator, domain='QQ')
        print(f"商: {quotient}")
        print(f"余数: {remainder}")
        if quotient != 0:
            result.append(quotient)

        # 将余数作为新的分子进行部分分式分解
        numerator = remainder
    roots = sp.roots(denominator, x)
    print(roots)
    solution_denominator = []
    for root, multiplicity in roots.items():
        solution_denominator.extend([root] * multiplicity)
    numerator_degree = sp.Poly(numerator, x).degree()
    denominator_degree = sp.Poly(denominator, x).degree()
    # 如果分子最高幂次数小于分母最高幂次数
    if numerator_degree < denominator_degree:
        for i, root in enumerate(roots):
            temp = numerator
            for j, other_root in enumerate(roots):
                if j != i:
                    temp = temp / ((x - other_root) ** roots[other_root])
            A = numerator / temp
            A = A.subs(x, root) / ((x - root) ** roots[root])
            result.append(A)
        result = [i for i in result if i != 0]  # 删除为0的结果
        for i in range(len(result)):
            print(f"部分分式{i}为: {result[i]}")

        return result, True


if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    root.title("部分分式计算器")
    tk.Label(root, text="欢迎来到分式计算器，请按照x**2+x*2或x^2类似方式输入", foreground="red", font=("Arial", 16)).pack(
        pady=10)
    # 创建输入框和标签
    tk.Label(root, text="请输入有理分式的分子:", foreground="green", font=("Arial", 16)).pack(pady=10)
    numerator_entry = tk.Entry(root, width=50)
    numerator_entry.pack(pady=10)

    # 分母输入框和标签
    tk.Label(root, text="请输入有理分式的分母:", foreground="green", font=("Arial", 16)).pack(pady=10)
    denominator_entry = tk.Entry(root, width=50)
    denominator_entry.pack(pady=10)

    # 创建计算按钮
    button = tk.Button(root, text="计算部分分式", foreground="blue", font=("Arial", 12), width=30, command=on_calculate)
    button.pack(pady=10)

    # 创建结果标签
    result_label = tk.Label(root, text="", foreground="red", bd=5)
    result_label.pack(pady=10)

    # 运行主循环
    root.mainloop()
