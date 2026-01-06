with open('Day 7//Day 7 input.txt') as raw:
    raw_input = raw.read().splitlines()

grid = [list(raw_input[i]) for i in range(len(raw_input))]
start = [grid[0].index('S')]
number_of_times_split=0

for i in range(1,len(grid)):
    starting_positions = []
    for s in start:
        if grid[i][s] == '^':
            number_of_times_split+=1
            if grid[i][s - 1]:
                grid[i][s - 1] = '|'
                starting_positions.append(s - 1)
            if grid[i][s + 1]:
                grid[i][s + 1] = '|'
                starting_positions.append(s + 1)
        elif grid[i][s] == '.':
            grid[i][s] = '|'
            starting_positions.append(s)
    start = set(starting_positions)
print(number_of_times_split)
#1590