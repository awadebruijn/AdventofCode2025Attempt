import re
import math
with open('Day 6//Day 6 input.txt') as raw:
    raw_input = raw.read().splitlines()

numbers = [[int(x) for x in line] for line in [re.findall(r'\d+',line) for line in raw_input[:-1]]]
operations = re.findall(r"\S+", raw_input[-1])

operation_results = []
for i in range(len(numbers[0])):
    if operations[i] == '*':
        operation_results.append(math.prod([numbers[j][i] for j in range(len(raw_input)-1)]))
    elif operations[i] == '+':
        operation_results.append(sum([numbers[j][i] for j in range(len(raw_input)-1)]))
print(sum(operation_results))
#4648618073226