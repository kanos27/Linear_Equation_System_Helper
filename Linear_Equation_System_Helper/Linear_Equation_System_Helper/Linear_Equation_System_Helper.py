

class equation():
    def __init__(self, factors, second_member):
        self.factors = factors
        self.second_member = second_member

    def __str__(self):
        equation_text = ""
        for i in range(len(self.factors)):
            if i == 0 :
                equation_text += str(self.factors[i]) + "x" + str(i+1)
            else :
                equation_text += " + " + str(self.factors[i]) + "x" + str(i+1)
        equation_text += " = " + self.second_member

        return equation_text

    def __mul__(self, scaler):
        for factor in range(len(self.factors)):
            self.factors[factor]*= scaler

    def __add__(self, other):
        for factor in range(len(self.factors)):
            self.factors[factor] += other.factors[factor]*scaler


class equation_system():
    def __init__(self, equations, nbr_of_unknown, second_members):
        self.equations = equations
        self.nbr_of_unknown = nbr_of_unknown
        ...

    def __str__(self):
        system_text = ""
        system_text += "---\n" #basic system layout
        for eq in self.equations:
            system_text+= str(eq) + "\n"

        system_text += "---\n" #basic system layout
        return system_text

    def swap_equations(self, index1, index2):
        self.equations[index1], self.equations[index2] = self.equations[index2], self.equations[index2]


def main():
    ...

if __name__ == "__main__":
    main()