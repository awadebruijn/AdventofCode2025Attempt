import re
with open('Anna\'s solutions//Day 1//Day 1 input.txt') as raw:
    raw_input = raw.read().splitlines()

shift = [int(x) for line in [re.findall(r'\d+', line) for line in raw_input] for x in line]

position_dial = 50
counter_at0 = 0

for i in range(len(shift)):

    if raw_input[i][0] == 'R':
        passing_0 = (position_dial + shift[i]) // 100
        position_dial += shift[i]
    else:
        if position_dial != 0:
            passing_0 = (shift[i] + (100 - position_dial)) // 100
        else:
            passing_0 = shift[i] // 100
        position_dial -= shift[i]

    if passing_0 != 0:
        counter_at0 += passing_0

    position_dial %= 100
print(counter_at0)
#2235 too low
#5847