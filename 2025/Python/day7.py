from collections import deque
from datetime import datetime

def getData(test=False):
    if test:
        data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
    else:
        with open("./2025/data/7.txt", 'r') as file:
            data = file.read()
    
    return [list(x) for x in data.split("\n") if x]


data = getData(test=True)
splits = 0

for row_index, row in enumerate(data[:-1]):
    print(row)
    next_row = data[row_index+1]
    for index, value in enumerate(row):
        if value in ["S", "|"]:
            if next_row[index] == "^":
                next_row[index-1] = "|"
                next_row[index+1] = "|"
                splits += 1
            else:
                next_row[index] = "|"
            
                    
print(data[-1])
beams = sum([x=="|" for x in data[-1]])
print(f"Part one: {splits}")

data = getData(test=False)

from collections import defaultdict

paths = defaultdict(lambda: defaultdict(int))

for col, value in enumerate(data[0]):
    if value == "S":
        paths[0][col] = 1

for row in range(len(data) -1):
    next_row = data[row + 1]
    
    for col, count in paths[row].items():
        if next_row[col] == "^":
            # We Splitting
            if col -1 >=0:
                paths[row + 1][col - 1] += count
            if col +1 < len(next_row):
                paths[row + 1][col + 1] += count
        else:
            paths[row + 1][col] += count

# print(paths)

last_row = len(data) -1 
total_paths = sum(paths[last_row].values())

print(f"Part Two: {total_paths}")
