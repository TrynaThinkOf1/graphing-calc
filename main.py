import numpy as np
import matplotlib.pyplot as plt
import re

class Graph:
    def __init__(self, equation: str):
        self.equation = equation
        print(self.frosting())

    #baking a cake, layer by layer
    def frosting(self):
        tokens = re.split(r"(\+|\-)", self.equation)

        equation = []

        for token in tokens:
            if token in {"+", "-"}:
                equation.append(token)
            else:
                equation.append(self.cake(token))
        return equation

    def cake(self, token):
        if "^" in token:
            base, power = token.split("^")
            return [self.plate(base), "**", self.plate(power)]

        elif re.match(r'[a-zA-Z]\w*', token) and len(token) > 1:
            return [token[0], "*", self.plate(token[1:])]
        else:
            return token

    def plate(self, token):
        return token


graph = Graph("ax^2+bx+c")