import re
with open('Anna\'s solutions//Day 2//Day 2 input.txt') as raw:
    raw_input = raw.read().split(',')

IDs = [[int(x) for x in line] for line in [re.findall(r'\d+', line) for line in raw_input]]
invalid_IDs = []

for ID_range in IDs:
    ID = ID_range[0]

    while ID < ID_range[1] + 1:
        list_of_digits = [int(d) for d in str(ID)]
        if list_of_digits[:(len(list_of_digits) // 2)] == list_of_digits[(len(list_of_digits) // 2):]:
            invalid_IDs.append(ID)
        ID += 1
print(sum(invalid_IDs))
#29818212493