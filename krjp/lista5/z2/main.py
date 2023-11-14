class Formula:

    def __init__(self, formula):
        self.formula = formula

    def __add__(self, other):
        return Or(self, other)

    def __mul__(self, other):
        return And(self, other)

    @classmethod
    def uprosc(cls, formula):
        if isinstance(formula, And):
            f1 = cls.uprosc(formula.formula1)
            f2 = cls.uprosc(formula.formula2)
            if (isinstance(f1, Stala) and not f1.value) or (isinstance(f2, Stala) and not f2.value):
                return Stala(False)
            elif isinstance(f1, Stala) and f1.value:
                return f2
            elif isinstance(f2, Stala) and f2.value:
                return f1
            else:
                return And(f1, f2)
        elif isinstance(formula, Or):
            f1 = cls.uprosc(formula.formula1)
            f2 = cls.uprosc(formula.formula2)
            if (isinstance(f1, Stala) and f1.value) or (isinstance(f2, Stala) and f2.value):
                return Stala(True)
            elif isinstance(f1, Stala) and not f1.value:
                return f2
            elif isinstance(f2, Stala) and not f2.value:
                return f1
            else:
                return Or(f1, f2)
        elif isinstance(formula, Not):
            f = cls.uprosc(formula.formula)
            if isinstance(f, Stala):
                return Stala(not f.value)
            else:
                return Not(f)
        else:
            return formula


class BadFormulaException(Exception):
    pass


class Or(Formula):
    
    def __init__(self, formula1, formula2):
        self.formula1 = formula1
        self.formula2 = formula2

    def oblicz(self, zmienne):
        return self.formula1.oblicz(zmienne) or self.formula2.oblicz(zmienne)

    def __str__(self):
        return "(" + str(self.formula1) + " + " + str(self.formula2) + ")"


class And(Formula):

    def __init__(self, formula1, formula2):
        self.formula1 = formula1
        self.formula2 = formula2

    def oblicz(self, zmienne):
        return self.formula1.oblicz(zmienne) and self.formula2.oblicz(zmienne)

    def __str__(self):
        return "(" + str(self.formula1) + " * " + str(self.formula2) + ")"
    

class Not(Formula):

    def __init__(self, formula):
        self.formula = formula

    def oblicz(self, zmienne):
        return not self.formula.oblicz(zmienne)

    def __str__(self):
        return "!" + str(self.formula)


class Zmienna(Formula):

    def __init__(self, name):
        self.name = name

    def oblicz(self, zmienne):
        if self.name not in zmienne:
            raise BadFormulaException("Nie znaleziono zmiennej " + self.name)
        return zmienne[self.name]

    def __str__(self):
        return self.name

class Stala(Formula):
        
    def __init__(self, value):
        if not isinstance(value, bool):
            raise BadFormulaException("Stala musi byc typu bool")
        self.value = value

    def oblicz(self, zmienne):
        return self.value

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    przykladowa_formula_1 = Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True)))
    print("Formuła 1: " + str(przykladowa_formula_1))
    zmienne_1 = {"x": True, "y": True}
    print("Wynik dla x = True i y = True: " + str(przykladowa_formula_1.oblicz(zmienne_1)))
    uprosc_przykladowa_formula_1 = Formula.uprosc(przykladowa_formula_1)
    print("Uproszczona formuła 1: " + str(uprosc_przykladowa_formula_1))
    print("Wynik uproszczonej formuły 1: " + str(uprosc_przykladowa_formula_1.oblicz(zmienne_1)))

    print()

    przykladowa_formula_2 = Stala(True) * Or(And(Zmienna("x"), Stala(False)), Zmienna("y"))
    print("Formuła 2: " + str(przykladowa_formula_2))
    zmienne_2 = {"x": True, "y": False}
    print("Wynik dla x = True i y = False: " + str(przykladowa_formula_2.oblicz(zmienne_2)))
    uprosc_przykladowa_formula_2 = Formula.uprosc(przykladowa_formula_2)
    print("Uproszczona formuła 2: " + str(uprosc_przykladowa_formula_2))
    print("Wynik uproszczonej formuły 2: " + str(uprosc_przykladowa_formula_2.oblicz(zmienne_2)))

    # Błędne formuły:

    #przykladowa_formula_3 = Not(Stala("a"))
    
    #przykladowa_formula_4 = And(Stala(True), Zmienna("x"))
    #zmienne_4 = {"y": False}
    #print(przykladowa_formula_4.oblicz(zmienne_4))
