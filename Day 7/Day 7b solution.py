from collections import Counter
with open('Day 7//Day 7 input.txt') as raw:
    raw_input = raw.read().splitlines()

grid = [list(raw_input[i]) for i in range(len(raw_input))]
starting_positions = [grid[0].index('S')]
timeline = Counter(starting_positions)

for i in range(1,len(grid)):
    start = list(set(starting_positions))
    starting_positions = []
    for s in start:
        if grid[i][s] == '^':
            if grid[i][s - 1]:
                grid[i][s - 1] = '|'
                starting_positions.append(s - 1)
                timeline[s - 1] += timeline[s] 
            if grid[i][s + 1]:
                grid[i][s + 1] = '|'
                starting_positions.append(s + 1)
                timeline[s + 1] += timeline[s]
            timeline[s] = 0
        else:
            grid[i][s] = '|'
            starting_positions.append(s)

number_of_timelines = sum([timeline[i] for i in timeline])
print(number_of_timelines)

resulting_grid=["".join(grid[i]) for i in range(len(grid))]
print("\n".join(resulting_grid))
#20571740188555