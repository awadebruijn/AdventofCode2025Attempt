import re
with open('Day 2//Day 2 input.txt') as raw:
    raw_input = raw.read().split(',')

IDs = [[int(x) for x in line] for line in [re.findall(r'\d+', line) for line in raw_input]]
invalid_IDs = []

for ID_range in IDs:
    ID = ID_range[0]

    while ID < ID_range[1] + 1:
        list_of_digits = [int(d) for d in str(ID)]
        number_of_occurences = list_of_digits.count(list_of_digits[0])

        for chunk_size in range(1, len(list_of_digits)):
            if len(list_of_digits) % chunk_size == 0:
                number_of_chunks = len(list_of_digits) // chunk_size
                list_chunks = [list_of_digits[j * chunk_size:(j + 1) * chunk_size] for j in range(number_of_chunks)]
                if all(chunk == list_of_digits[:chunk_size] for chunk in list_chunks):
                    invalid_IDs.append(ID)
                    break
        ID += 1
print(sum(invalid_IDs))
#37432260594
