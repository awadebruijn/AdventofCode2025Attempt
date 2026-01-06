import re
import math
with open('Day 6//Day 6 input.txt') as raw:
    raw_input = raw.read().splitlines()

original_numbers = [[x for x in line] for line in raw_input[:-1]]
numbers = [[original_numbers[j][i] for j in range(len(original_numbers))] for i in range(len(original_numbers[0]))]
operations = re.findall(r"\S+", raw_input[-1])

string_integers = []
for i in range(len(numbers)):
    string_integers.append("".join([n.replace(" ","") for n in numbers[i]]))

integers = []
current = []
for item in string_integers:
    if item == '':
        integers.append(current)
        current = []
    else:
        current.append(int(item))
if current:
    integers.append(current)

resulting_list = []
for i in range(len(operations)):
    if operations[i] == '*':
        resulting_list.append(math.prod(integers[i]))
    elif operations[i] == '+':
        resulting_list.append(sum(integers[i]))
print(sum(resulting_list))
#7329921182115