from determinant import Determinant
from matrix import Matrix
from config import Config
from graphic import Graphic


if __name__ == '__main__':
    determinant = Determinant()
    roots = determinant.root_search()
    # print(roots)

    wave_equations = ""
    for i in range(len(roots)):
        matrix = Matrix(roots[i])
        coefficients = matrix.solve()

        if i != 0:
            wave_equations += "\n"
        wave_equations += Config.psi_upper + "_" + str(i + 1) + " = "
        for j in range(len(coefficients)):
            if coefficients[j] < 0:
                wave_equations += "("
            wave_equations += str(round(coefficients[j], 5)) + " * " + Config.psi + "_" + str(j + 1)
            if coefficients[j] < 0:
                wave_equations += ")"

            if j != len(coefficients) - 1:
                wave_equations += " + "

    Graphic(wave_equations).get()
