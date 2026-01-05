with open('Anna\'s solutions//Day 3//Day 3 input.txt') as raw:
    raw_input = raw.read().splitlines()

highest_twelves = []
for bank in raw_input:
    list_bank = [int(jolt) for jolt in bank]

    highest_twelve = []
    ith_index = 0
    for i in range(11):
        ith_entry = max(list_bank[ith_index:-11 + i])
        ith_index = list_bank[ith_index:].index(ith_entry) + ith_index + 1
        highest_twelve.append(str(ith_entry))
    ith_entry = max(list_bank[ith_index:])
    highest_twelve.append(str(ith_entry))

    highest_twelves.append(int("".join(highest_twelve)))
print(sum(highest_twelves))
#171435596092638


