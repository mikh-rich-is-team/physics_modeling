import sympy
import sympy as sym


class Determinant:
    __ALPHA = -11.0
    __BETA = -2.4

    def __init__(self):
        self.determinant = [["x", "1", "0", "0", "0", "0", "0", "0", "0", "1"],
                            ["1", "x", "1", "0", "0", "0", "0", "0", "0", "0"],
                            ["0", "1", "x", "1", "0", "0", "0", "0", "0", "0"],
                            ["0", "0", "1", "x", "1", "0", "0", "0", "0", "0"],
                            ["0", "0", "0", "1", "x", "1", "0", "0", "0", "1"],
                            ["0", "0", "0", "0", "1", "x", "1", "0", "0", "0"],
                            ["0", "0", "0", "0", "0", "1", "x", "1", "0", "0"],
                            ["0", "0", "0", "0", "0", "0", "1", "x", "1", "0"],
                            ["0", "0", "0", "0", "0", "0", "0", "1", "x", "1"],
                            ["1", "0", "0", "0", "1", "0", "0", "0", "1", "x"]]
        #
        # self.determinant = [["x", "3", "1"],
        #                     ["2", "4", "x"],
        #                     ["x", "x", "0"]]
        #
        # self.determinant = [["8 * x", "3", "2"],
        #                     ["4", "x", "3"],
        #                     ["x", "5 * x", "1"]]

    def root_search(self):
        determinant_decomposition = self.decomposition_to_string(len(self.determinant), [], "")

        x = sym.Symbol('x')
        expr = sym.simplify(determinant_decomposition)

        result = sym.solveset(expr, x, sympy.Reals)

        answers = []
        for m in result:
            answers.append(self.get_E(sym.N(m)))

        return answers

    def decomposition_to_string(self, N, skipping, add_in_skipping):
        decomposition = ""
        skipping.append(add_in_skipping)

        start_position = len(self.determinant) - N
        if N > 2:
            for i in range(len(self.determinant)):
                skipping_flag = True
                for j in range(len(skipping)):
                    if i == skipping[j]:
                        skipping_flag = False

                if skipping_flag:
                    current_element = self.determinant[start_position][i]

                    if current_element != "0":
                        if (start_position + i) % 2 == 0:
                            add_plus_or_minus = " + "
                        else:
                            add_plus_or_minus = " - "

                        if len(decomposition) == 0:
                            if add_plus_or_minus == " + ":
                                add_plus_or_minus = ""
                            else:
                                add_plus_or_minus = "-"

                        get_result = self.decomposition_to_string(N - 1, skipping, i)

                        if len(get_result) > 0:
                            decomposition = decomposition + \
                                            add_plus_or_minus + \
                                            current_element + \
                                            " * (" + \
                                            get_result + \
                                            ")"

        if N == 2:
            calculating = []
            for i in range(len(self.determinant)):
                skipping_flag = True
                for j in range(len(skipping)):
                    if i == skipping[j]:
                        skipping_flag = False

                if skipping_flag:
                    calculating.append(self.determinant[start_position][i])
                    calculating.append(self.determinant[start_position + 1][i])

            first_miss = False
            second_miss = False
            for i in range(4):
                if calculating[i] == "0":
                    if (i == 0) or (i == 3):
                        first_miss = True
                    else:
                        second_miss = True

            # print(calculating[0] + " * " + calculating[3] + " - " + calculating[1] + " * " + calculating[2])
            skipping.pop()

            if first_miss and second_miss:
                return ""

            if first_miss:
                return "-" + calculating[1] + " * " + calculating[2]

            if second_miss:
                return calculating[0] + " * " + calculating[3]

            return calculating[0] + " * " + calculating[3] + " - " + calculating[1] + " * " + calculating[2]

        if len(skipping) > 0:
            skipping.pop()
        return decomposition

    def get_E(self, x):
        return self.__ALPHA - self.__BETA * x
