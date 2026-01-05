import re
with open('Anna\'s solutions//Day 2//Day 2 input.txt') as raw:
    raw_input = raw.read().split(',')

IDs = [[int(x) for x in line] for line in [re.findall(r'\d+', line) for line in raw_input]]
invalid_IDs = []

def is_repeated_pattern(s: str) -> bool:
    return s in (s + s)[1:-1]

for ID_range in IDs:
    ID = ID_range[0]

    while ID < ID_range[1] + 1:
        list_of_digits = [int(d) for d in str(ID)]
        number_of_occurences = list_of_digits.count(list_of_digits[0])
        if is_repeated_pattern(str(ID)):
            invalid_IDs.append(ID)
        ID += 1
print(sum(invalid_IDs))
#37432260594