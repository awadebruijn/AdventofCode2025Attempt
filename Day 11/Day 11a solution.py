import re
from copy import deepcopy
with open('Day 11//Day 11 input.txt') as raw:
    raw_input = raw.read().splitlines()

triplets = {re.findall(r'[a-z]+', line)[0] : re.findall(r'[a-z]+', line)[1:] for line in raw_input}

count = 0
start = triplets['you']

while len(start) > 0:
    end = []

    for triple in start:

        if triple == 'out':
            count += 1

        else:
            end.extend(triplets[triple])

    start = deepcopy(end)

print(count)
#574