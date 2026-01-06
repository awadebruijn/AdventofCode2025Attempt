import re
from shapely import Polygon
from shapely import LinearRing
with open('Day 9//Day 9 input.txt') as raw:
    raw_input = raw.read().splitlines()

corner_points = [[int(x) for x in coordinates] for coordinates in [re.findall(r'\d+', coordinates) for coordinates in raw_input]]
polygon = Polygon(corner_points)
areas = []

for i in range(len(corner_points)):
    for j in range(i + 1, len(corner_points)):
        rectangle = LinearRing([corner_points[i], [corner_points[j][0], corner_points[i][1]], corner_points[j], [corner_points[i][0], corner_points[j][1]]])
        if polygon.covers(rectangle):
            width = abs(corner_points[i][0] - corner_points[j][0]) + 1
            length = abs(corner_points[i][1] - corner_points[j][1]) + 1
            area = width * length
            areas.append(area)

print(max(areas))
#1577956170