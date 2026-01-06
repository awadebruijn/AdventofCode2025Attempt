import re
from itertools import combinations

def subsets_of_size(lst, k):
    return list(combinations(lst, k))

with open('Day 10//Day 10 mock input.txt') as raw:
    raw_input = raw.read().splitlines()

light_diagram = [re.findall(r'[#.]', line) for line in raw_input]
converted_light_diagram = [[i for i in range(len(diagram)) if list(diagram)[i] == '#'] for diagram in light_diagram]

buttons = [[re.findall(r'\d+', button) for button in line] for line in [re.findall(r'\(\S+\)', line) for line in raw_input]]
converted_buttons = [[[int(position) for position in positions] for positions in line] for line in buttons]
 
buttons_needed = []
for i in range(len(converted_buttons)):
    for j in range(1, len(converted_buttons[i])):
        pushes = subsets_of_size(converted_buttons[i], j)
        check = [[int(x) for x in re.findall(r'\d+', str(push))] for push in pushes]
        for k in range(len(check)):
            odd_appearances = sorted(set([x for x in check[k] if check[k].count(x) % 2 == 1]))
            if converted_light_diagram[i] == odd_appearances:
                buttons_needed.append(j)
                break
        if len(buttons_needed) > i:
            break
print(sum(buttons_needed))
#481