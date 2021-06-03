import copy

from config import Config
import sympy as sym


class Matrix:
    def __init__(self, x):
        # string_matrix = Config.string_matrix
        #
        # matrix = []
        # for i in range(len(string_matrix)):
        #     matrix_line = []
        #     for j in range(len(Config.string_matrix)):
        #         if string_matrix[i][j] == "x":
        #             matrix_line.append(x)
        #         else:
        #             matrix_line.append(float(string_matrix[i][j]))
        #     matrix.append(matrix_line)
        #
        # self.matrix = matrix
        self.x = x

    def solve(self):
        # a = self.matrix
        # b = [0] * len(self.matrix)
        #
        # result = self.lu_solve(a, b)
        c = self.get_c_1()[0]
        x = self.x

        expr_like_c_10 = (x ** 9 - 8 * x ** 7 + 21 * x ** 5 - 20 * x ** 3 + 5 * x) / (
                    x ** 8 - 7 * x ** 6 + 16 * x ** 4 - 13 * x ** 2 + 3)

        solve = []
        solve.append(c)
        solve.append(-c*x + c*expr_like_c_10)
        solve.append(c*(x**2 - 1) - c*x*expr_like_c_10)
        solve.append(-c*(x**3 - 2*x) + c*(x**2 - 1)*expr_like_c_10)
        solve.append(c*(x**4 - 3*x**2 + 1) - c*(x**3 - 2*x)*expr_like_c_10)
        solve.append(-c*(x**5 - 4*x**3 + 3*x) - c*(-(x**4) + 3*x**2 - 2)*expr_like_c_10)
        solve.append(c*(x**6 - 5*x**4 + 6*x**2 - 1) - c*(x**5 - 4*x**3 + 4*x)*expr_like_c_10)
        solve.append(c*(-(x**7) + 6*x**5 - 10*x**3 + 4*x) - c*(-(x**6) + 5*x**4 - 7*x**2 + 2)*expr_like_c_10)
        solve.append(c*(x**8 - 7*x**6 + 15*x**4 - 10*x**2 + 1) - c*(x**7 - 6*x**5 + 11*x**3 - 6*x)*expr_like_c_10)
        solve.append(c*expr_like_c_10)

        return solve

    def get_c_1(self):
        c = sym.Symbol('c')
        x = self.x

        expr_like_c_10 = (x**9 - 8*x**7 + 21*x**5 - 20*x**3 + 5*x) / (x**8 - 7*x**6 + 16*x**4 - 13*x**2 + 3)

        expr_c_1 = c**2
        expr_c_2 = (-c*x + c*expr_like_c_10)**2
        expr_c_3 = (c*(x**2 - 1) - c*x*expr_like_c_10)**2
        expr_c_4 = (-c*(x**3 - 2*x) + c*(x**2 - 1)*expr_like_c_10)**2
        expr_c_5 = (c*(x**4 - 3*x**2 + 1) - c*(x**3 - 2*x)*expr_like_c_10)**2
        expr_c_6 = (-c*(x**5 - 4*x**3 + 3*x) - c*(-(x**4) + 3*x**2 - 2)*expr_like_c_10)**2
        expr_c_7 = (c*(x**6 - 5*x**4 + 6*x**2 - 1) - c*(x**5 - 4*x**3 + 4*x)*expr_like_c_10)**2
        expr_c_8 = (c*(-(x**7) + 6*x**5 - 10*x**3 + 4*x) - c*(-(x**6) + 5*x**4 - 7*x**2 + 2)*expr_like_c_10)**2
        expr_c_9 = (c*(x**8 - 7*x**6 + 15*x**4 - 10*x**2 + 1) - c*(x**7 - 6*x**5 + 11*x**3 - 6*x)*expr_like_c_10)**2
        expr_c_10 = (c*expr_like_c_10)**2

        expr = sym.simplify(
            expr_c_1 + expr_c_2 + expr_c_3 + expr_c_4 + expr_c_5 + expr_c_6 + expr_c_7 + expr_c_8 + expr_c_9 + expr_c_10
        )

        result = sym.solveset(expr - 1, c)
        answers = []
        for m in result:
            answers.append(sym.N(m))

        return answers

    # def lu_solve(self, a, b):
    #     """Решение СЛАУ вида Ax=b с использованием LU-разложения методом Гаусса
    #
    #     :param a: матрица А
    #
    #     :param b: столбец свободных членов b
    #
    #     :return: столбец ответов x
    #     """
    #     res = self.lu_decompose()  # метод из matrix.py
    #     l_matrix = res[0]
    #     u_matrix = res[1]
    #
    #     # решение уравнения Ly=b
    #     y = [0 for _ in range(len(self.matrix))]
    #
    #     for i in range(len(l_matrix)):
    #         matrix_sum = b[i]
    #         for j in range(0, i):
    #             matrix_sum -= y[j] * l_matrix[i][j]
    #
    #         y[i] = matrix_sum / l_matrix[i][i]
    #
    #     # решение уравнения Ux=y
    #     x = [0 for _ in range(len(a))]
    #
    #     for i in range(len(u_matrix) - 1, -1, -1):
    #         matrix_sum = y[i]
    #         for j in range(len(u_matrix) - 1, i, -1):
    #             matrix_sum -= x[j] * u_matrix[i][j]
    #
    #         x[i] = matrix_sum / u_matrix[i][i]
    #
    #     return x
    #
    # def lu_decompose(self):
    #     """Метод разложения матрицы на произведение LU
    #
    #     :return: матрица L, матрица U
    #     """
    #     # заполнение матрицы нулями (размера width x height)
    #     l_matrix = [[0.0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix))]
    #     u_matrix = [[0.0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix))]
    #
    #     # заполнение матриц по формулам
    #     for i in range(0, len(self.matrix)):
    #         # заполнение U матрицы по формуле
    #         for j in range(i, len(self.matrix)):
    #             u_matrix[i][j] = self.matrix[i][j] - sum(l_matrix[i][k] * u_matrix[k][j] for k in range(0, i))
    #
    #         # заполнение L матрицы по формуле
    #         for j in range(i, len(self.matrix)):
    #             if i == j:
    #                 l_matrix[i][i] = 1  # заполняем единичками диагональ в L матрице
    #             else:
    #                 l_matrix[j][i] = (self.matrix[j][i] - sum(l_matrix[j][k] * u_matrix[k][i] for k in range(0, i))) / \
    #                                  u_matrix[i][i]
    #
    #     return l_matrix, u_matrix
