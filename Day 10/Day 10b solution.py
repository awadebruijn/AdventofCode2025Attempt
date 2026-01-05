import re
from functools import lru_cache
from itertools import combinations
with open('Anna\'s solutions//Day 10//Day 10 mock input.txt') as raw:
    raw_input = raw.read().splitlines()

buttons = [[[int(x) for x in re.findall(r'\d+', button)] for button in line] for line in [re.findall(r'\(\S+\)', line) for line in raw_input]]
joltage_levels = [[int(x) for x in re.findall(r'\d+', str(re.findall(r'{\S+}', line)))] for line in raw_input]

#@lru_cache(maxsize=256)
def subsets_of_size(lst, k):
  return list(combinations(lst, k))

#@lru_cache(maxsize=256)
def building_blocks(mod_joltage, button):
  for j in range(1, len(button)):
    converted_joltage_level = [k for k in range(len(mod_joltage)) if mod_joltage[k] == 1]
    pushes = subsets_of_size(button, j)
    check = [[int(x) for x in re.findall(r'\d+', str(push))] for push in pushes]
    for k in range(len(check)): 
      experiment = [check[k].count(x) for x in range(len(mod_joltage))]
      odd_appearances = sorted(set([x for x in check[k] if check[k].count(x) % 2 == 1]))
      if converted_joltage_level == odd_appearances:
        return j, experiment 
      
#example_mod_joltage = [1, 1, 0]
#example_buttons = [[0], [0, 1], [0, 1, 2]]
#result = building_blocks(example_mod_joltage, example_buttons)

###########################################################################################

totals = []
for i in range(len(joltage_levels)):
  n = 0
  total = 0
  while sum(joltage_levels[i]) != 0:
    residue = [x % 2 for x in joltage_levels[i]]
    number_of_blocks, experiment = building_blocks(residue, buttons[i])
    if type(number_of_blocks) == int:
      total += number_of_blocks * 2 ** n
    joltage_levels[i] = [(joltage_levels[i][j] - experiment[j]) // 2 for j in range(len(joltage_levels[i]))]
    n += 1
  totals.append(total)
print(totals)

##########################################################################################

#@lru_cache(maxsize=256)
#def f(arg):
#  a_list = list(arg)
#  return tuple(a_list)


#example = (3, 5, 4, 7)
#print(tuple(x for x in example))
#print(f(example))

##########################################################################################