#Import fractions

class Equation():
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
        equation_text += " = " + str(self.second_member)

        return equation_text

    def __mul__(self, scaler):
        new_equation = self.copy()
        for factor in range(len(self.factors)):
            new_equation.factors[factor] = self.factors[factor] * scaler
        new_equation.second_member = self.second_member * scaler
        return new_equation

    def __rmul__(self, scaler):
        new_equation = self.copy()
        for factor in range(len(self.factors)):
            new_equation.factors[factor] = self.factors[factor] * scaler
        new_equation.second_member = self.second_member * scaler
        return new_equation

    def __add__(self, other):
        new_equation = self.copy()
        for factor in range(len(self.factors)):
            new_equation.factors[factor] = self.factors[factor] + other.factors[factor]
        new_equation.second_member = self.second_member + other.second_member
        return new_equation

    def __sub__(self,other):
        new_equation = self.copy()
        for factor in range(len(self.factors)):
            new_equation.factors[factor] = self.factors[factor] - other.factors[factor]
        new_equation.second_member = self.second_member - other.second_member
        return new_equation

    def copy(self):
        new_equation = Equation([n for n in self.factors], self.second_member)
        return new_equation

class Equation_system():
    def __init__(self, equations, nbr_of_unknown):
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
    eq1 = Equation([1, 1, 2], 3)
    print(eq1)
    eq2 = Equation ([3, 0, 5], 7)

    sys1 = Equation_system([eq1, eq2], 3)
    print(sys1)
    sys1.equations[0] = sys1.equations[0]*2
    print(sys1)
    sys1.equations[0] = sys1.equations[0] - sys1.equations[1]
    print(sys1)
    sys1.equations[0] = sys1.equations[0] - (2*sys1.equations[1])
    print(sys1)

if __name__ == "__main__":
    main()