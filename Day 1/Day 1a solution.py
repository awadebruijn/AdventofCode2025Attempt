import re
with open('Anna\'s solutions//Day 1//Day 1 input.txt') as raw:
    raw_input = raw.read().splitlines()

shift = [int(x) for line in [re.findall(r'\d+', line) for line in raw_input] for x in line]

position_dial = 50
counter_at0 = 0

for i in range(len(shift)):
    if raw_input[i][0] == 'R':
        position_dial += shift[i]
    else:
        position_dial -= shift[i]
    if position_dial % 100 == 0:
        counter_at0 += 1
print(counter_at0)
#995