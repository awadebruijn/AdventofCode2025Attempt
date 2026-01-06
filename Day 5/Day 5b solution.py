import re
with open('Day 5//Day 5 input.txt') as raw:
    raw_input = raw.read().split("\n\n")

fresh_ingredient_ID_ranges = [re.findall(r'\d+',ID_range) for ID_range in raw_input[0].split("\n")]
ordered_fresh_ingredient_ID_ranges = sorted([[int(x[0]),int(x[1])] for x in fresh_ingredient_ID_ranges])

non_overlap_IDs = []
position = 0
ID_range = ordered_fresh_ingredient_ID_ranges[0]
while position < len(ordered_fresh_ingredient_ID_ranges) - 1:
    position += 1
    if ID_range[1] < ordered_fresh_ingredient_ID_ranges[position][1]:
        if ID_range[1] + 1 >= ordered_fresh_ingredient_ID_ranges[position][0]:
            ID_range = [ID_range[0],ordered_fresh_ingredient_ID_ranges[position][1]]
        else:
            non_overlap_IDs.append(ID_range)
            ID_range = ordered_fresh_ingredient_ID_ranges[position]
non_overlap_IDs.append(ID_range)

lengths_of_ranges = [abs(ID_range[1] - ID_range[0] + 1) for ID_range in non_overlap_IDs]
print(sum(lengths_of_ranges))
#314506327627848 too low
#340755374652935 too low
#353863745078671