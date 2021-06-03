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

        print(Config.psi_upper + " = ")
        for j in range(len(coefficients)):
            print(str(coefficients[j]) + " * " + Config.psi + "_" + str(j + 1) + " + ")
