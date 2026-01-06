import re
from functools import lru_cache
from itertools import combinations
from copy import deepcopy
with open('Day 10//Day 10 input.txt') as raw:
    raw_input = raw.read().splitlines()

buttons = tuple(tuple(tuple(int(x) for x in re.findall(r'\d+', button)) for button in line) for line in [re.findall(r'\(\S+\)', line) for line in raw_input])
joltage_levels = tuple(tuple(int(x) for x in re.findall(r'\d+', str(re.findall(r'{\S+}', line)))) for line in raw_input)

@lru_cache(maxsize=256)
def subsets_of_size(lst, k):
  return tuple(combinations(lst, k))

@lru_cache(maxsize=256)
def building_blocks(total, i):
  counts = []
  results = []

  for j in range(len(buttons[i])+1):
    residue = [x % 2 for x in total]
    converted_joltage_level = [k for k in range(len(residue)) if residue[k] == 1]
    pushes = subsets_of_size(tuple(buttons[i]), j)
    check = [[int(x) for x in re.findall(r'\d+', str(push))] for push in pushes]

    for k in range(len(check)): 
      button_sum = [check[k].count(x) for x in range(len(residue))]
      new_total = [(total[i] - button_sum[i]) // 2 for i in range(len(button_sum))]

      if min(new_total) >= 0:
        odd_appearances = sorted(set([x for x in check[k] if check[k].count(x) % 2 == 1]))

        if converted_joltage_level == odd_appearances: 
          counts.append(j)
          results.append(new_total)
          
  return tuple(counts), tuple(results) 

amount = []

for i in range(len(buttons)):
  n = 0
  totals = [[joltage_levels[i], 0]]

  while any(max(total[0]) != 0 for total in totals):
    new_totals = []

    for total in totals:
      counts, results = building_blocks(tuple(total[0]), i)

      for j in range(len(counts)):
        count = total[1] + counts[j] * 2 ** n
        new_totals.append([results[j], count])

    totals = deepcopy(new_totals)
    n += 1

  sub_counts = [total[1] for total in totals]
  amount.append(min(sub_counts))

print(sum(amount))
#20142