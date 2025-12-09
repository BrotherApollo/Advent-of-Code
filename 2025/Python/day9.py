test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".split("\n")
test = [(int(x), int(y)) for x,y in [item.split(",") for item in test]]
print(test)
rows = max([x[1] for x in test])
cols = max([x[0] for x in test])

grid = []
for row in range(rows+1):
    new_row = []
    for col in range(cols+1):
        if (col, row) in test:
            new_row.append("#")
        else:
            new_row.append(".")
    grid.append(new_row)

for row in grid:
    print("".join(row))


def squaresize(a, b):
    height = abs(a[1] -b[1]) + 1
    width = abs(a[0] -b[0]) + 1
    # print(height)
    # print(width)
    return width * height

print(squaresize(test[0], test[1]))

def findBiggest(data):
    biggest = 0
    for index, p1 in enumerate(data):
        for p2 in data[index:]:
            size = squaresize(p1, p2)
            if size > biggest:
                biggest = size
    return biggest

with open("./2025/data/9.txt", 'r') as file:
    data = file.read().split("\n")
    data = [(int(x), int(y)) for x,y in [item.split(",") for item in data]]

print(f"Part One: {findBiggest(data)}")

#Part two

from shapely.geometry import MultiPoint, Polygon
from shapely import wkt

bigpoly = Polygon(data)

print(f"Is valid: {bigpoly.is_valid}")
print(f"Is simple (no self-intersections): {bigpoly.is_simple}")

if not bigpoly.is_valid:
    from shapely.validation import explain_validity
    print(f"Validity issue: {explain_validity(bigpoly)}")

# print(bigpoly)

points = MultiPoint(data)
hull = points.convex_hull

def makePoly(a, b):
    min_x = min([a[0], b[0]])
    max_x = max([a[0], b[0]])
    min_y = min([a[1], b[1]])
    max_y = max([a[1], b[1]])

    points = [
        (min_x, min_y),  # bottom-left
        (max_x, min_y),  # bottom-right
        (max_x, max_y),  # top-right
        (min_x, max_y)   # top-left
    ]
    return Polygon(points)

biggest = 0
for index, p1 in enumerate(data):
    for p2 in data[index:]:
        poly = makePoly(p1,p2)
        if not poly.within(bigpoly):
            continue
        size = squaresize(p1, p2)
        if size > biggest:
            biggest = size

print(f"PartTwo: {biggest}")