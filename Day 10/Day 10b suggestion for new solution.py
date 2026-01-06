import re
import numpy as np
from sympy.solvers.solveset import linsolve
import sympy as sp
with open('Anna\'s solutions//Day 10//Day 10 mock input.txt') as raw:
    raw_input = raw.read().splitlines()

buttons = [[[int(x) for x in re.findall(r'\d+', button)] for button in line] for line in [re.findall(r'\(\S+\)', line) for line in raw_input]]
joltage_levels = [[int(x) for x in re.findall(r'\d+', str(re.findall(r'{\S+}', line)))] for line in raw_input]

#print(buttons)
#print(joltage_levels)

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sp.symbols('a:z', integer = True, negative = False)

#This would need to be automated
eqs = [e + f - 3, b + f - 5, c + d + e - 4, a + b + d - 7]
solution = list(list(linsolve(eqs, (a, b, c, d, e, f)))[0])
remaining_symbols = list(set().union(*(x.free_symbols for x in solution)))
upper_bound = max(joltage_levels[0])
print(sum(solution), solution)
print(remaining_symbols)
print(upper_bound)

#Creating symbols from a list of strings
#names = ["x", "y", "z"]
#symbols = sp.symbols(" ".join(names))
#print(symbols)

#Example of retrieving symbols from an equation
#exprs = [sp.sin(sp.Symbol("x")), sp.Symbol("y") + 3]
#all_symbols = list(set().union(*(e.free_symbols for e in exprs)))
#print(all_symbols)

#while all():