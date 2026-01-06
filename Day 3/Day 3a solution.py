with open('Day 3//Day 3 input.txt') as raw:
    raw_input = raw.read().splitlines()

banks = [[int(x) for x in bank]for bank in raw_input]
highest_pairs = []

for bank in banks:
    pairs_of_jolts = [int(str(bank[i]) + str(bank[i + 1:][j])) for i in range(len(bank) - 1) for j in range(len(bank) - i - 1)]
    highest_pair = sorted(pairs_of_jolts, reverse = True)[0]
    highest_pairs.append(highest_pair)
print(sum(highest_pairs))
#17244



