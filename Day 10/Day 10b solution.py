import re
from functools import lru_cache
from itertools import combinations
from copy import deepcopy
with open('Day 10//Day 10 mock input.txt') as raw:
    raw_input = raw.read().splitlines()

buttons = [[[int(x) for x in re.findall(r'\d+', button)] for button in line] for line in [re.findall(r'\(\S+\)', line) for line in raw_input]]
joltage_levels = [[int(x) for x in re.findall(r'\d+', str(re.findall(r'{\S+}', line)))] for line in raw_input]
print(len(buttons))

#@lru_cache(maxsize=256)
def subsets_of_size(lst, k):
  return list(combinations(lst, k))

#@lru_cache(maxsize=256)
def building_blocks(total, i):
  counts = []
  results = []

  for j in range(1, len(buttons[i])):
    residue = [x % 2 for x in total]
    converted_joltage_level = [k for k in range(len(residue)) if residue[k] == 1]
    pushes = subsets_of_size(buttons[i], j)
    check = [[int(x) for x in re.findall(r'\d+', str(push))] for push in pushes]

    for k in range(len(check)): 
      button_sum = [check[k].count(x) for x in range(len(residue))]
      new_total = [(total[i] - button_sum[i]) // 2 for i in range(len(button_sum))]
      if min(new_total) >= 0:
        odd_appearances = sorted(set([x for x in check[k] if check[k].count(x) % 2 == 1]))
        if converted_joltage_level == odd_appearances:
          counts.append(j)
          results.append(new_total)
  #print(counts, results)
  return counts, results 

###########################################################################################

amount = []

for i in range(len(buttons)):
  n = 0
  totals = [[joltage_levels[i], 0]]

  while any(max(total[0]) != 0 for total in totals):
    new_totals = []

    for total in totals:
      counts, results = building_blocks(total[0], i)

      for j in range(len(counts)):
        count = total[1] + counts[j] * 2 ** n
        new_totals.append([results[j], count])
    totals = deepcopy(new_totals)
    n += 1
  print(totals)
  sub_counts = [total[1] for total in totals]
  amount.append(min(sub_counts))
print(amount)

##########################################################################################