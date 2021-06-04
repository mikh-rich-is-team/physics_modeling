from determinant import Determinant
from matrix import Matrix
from config import Config


if __name__ == '__main__':
    determinant = Determinant()
    roots = determinant.root_search()
    print(roots)

    for i in range(len(roots)):
        matrix = Matrix(roots[i])
        coefficients = matrix.solve()

        print()
        print(Config.psi_upper + "_" + str(i + 1) + " = ", end='')
        for j in range(len(coefficients)):
            print(str(coefficients[j]) + " * " + Config.psi + "_" + str(j + 1), end='')
            if j != len(coefficients) - 1:
                print(" + ", end='')
