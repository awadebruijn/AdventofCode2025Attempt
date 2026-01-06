#Pythagoras in 3D: sqrt(a^2+b^2+c^2) where a is the difference in X, b in Y and c in Z coordinates.
import re
import math
with open('Day 8//Day 8 input.txt') as raw:
    raw_input = raw.read().splitlines()

positions = [[int(x) for x in re.findall(r'\d+', line)] for line in raw_input]
differences_squared = []

for i in range(len(positions) - 1):
    for j in range(i + 1,len(positions)):
        d_squared = (positions[i][0] - positions[j][0]) ** 2 + (positions[i][1] - positions[j][1]) ** 2 + (positions[i][2] - positions[j][2]) ** 2
        differences_squared.append([d_squared, [i,j]])

def in_same_sublist(lst, val1, val2):
    return any(val1 in sub and val2 in sub for sub in lst)

sorted_differences_squared = sorted(differences_squared, key = lambda x: x[0])

connections_attempted = 0
circuits = [[i] for i in range(len(positions))]

for value in sorted_differences_squared:
    connections_attempted += 1
    i = value[1][0]
    j = value[1][1]
    if connections_attempted <= 1000:
        if not in_same_sublist(circuits, i, j):
            position_of_i = next((k for k, sub in enumerate(circuits) if i in sub), None)
            position_of_j = next((k for k, sub in enumerate(circuits) if j in sub), None)
            circuits[position_of_i].extend(circuits[position_of_j])
            del circuits[position_of_j] 
    else:
        break

lengths_of_circuits = sorted(list(set([len(circuit) for circuit in circuits])), reverse = True)
print(math.prod(lengths_of_circuits[:3]))
#122636
