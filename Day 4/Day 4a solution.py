import re
with open('Anna\'s solutions//Day 4//Day 4 input.txt') as raw:
    raw_input = raw.read().splitlines()

grid = [[a for a in row] for row in raw_input]

#i is referring to ith row, j is referring to jth column
accessible_paper_rolls = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            counter = 0
            if i > 0: 
                if grid[i - 1][j] == '@':
                    counter += 1
            if i > 0 and j < len(grid[i]) - 1:
                if grid[i - 1][j + 1] == '@':
                    counter += 1
            if j < len(grid[i]) - 1:
                if grid[i][j + 1] == '@':
                    counter += 1
            if i < len(grid) - 1 and j < len(grid[i]) - 1: 
                if grid[i + 1][j + 1] == '@':
                    counter += 1
            if i < len(grid) - 1:
                if grid[i + 1][j] == '@':
                    counter += 1
            if i < len(grid) - 1 and j > 0:
                if grid[i + 1][j - 1] == '@':
                    counter += 1
            if j > 0: 
                if grid[i][j - 1] == '@':
                    counter += 1
            if i > 0 and j > 0:
                if grid[i - 1][j - 1] == '@':
                    counter += 1
            if counter < 4:
                accessible_paper_rolls += 1
print(accessible_paper_rolls)
#1435