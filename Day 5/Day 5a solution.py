import re
with open('Day 5//Day 5 input.txt') as raw:
    raw_input = raw.read().split("\n\n")

fresh_ingredient_ID_ranges = raw_input[0].split("\n")
available_ingredient_IDs = raw_input[1].split("\n")

fresh_ingredient_IDs = 0
for ingredient in available_ingredient_IDs:
    for ID_range in fresh_ingredient_ID_ranges:
        start_and_end = re.findall(r'\d+', ID_range)
        start = int(start_and_end[0])
        end = int(start_and_end[1]) + 1
        if start <= int(ingredient) <= end:
            fresh_ingredient_IDs += 1
            break
print(fresh_ingredient_IDs)
#782
