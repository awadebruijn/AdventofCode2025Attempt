import re
with open('Anna\'s solutions//Day 9//Day 9 input.txt') as raw:
    raw_input = raw.read().splitlines()

corner_points = [[int(x) for x in coordinates] for coordinates in [re.findall(r'\d+', coordinates) for coordinates in raw_input]]
rectangles = []

for i in range(len(corner_points)):
    for j in range(i + 1, len(corner_points)):
        width = abs(corner_points[i][0] - corner_points[j][0]) + 1
        length = abs(corner_points[i][1] - corner_points[j][1]) + 1
        area = width * length
        rectangles.append(area)

print(max(rectangles))
#4758121828