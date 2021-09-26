

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


class equation_system():
    def __init__(self, equations, nbr_of_unknown):
        self.equations = equations
        self.nbr_of_unknown = nbr_of_unknown
        ...

    def __str__(self):
        ...


def main():
    ...

if __name__ == "__main__":
    main()