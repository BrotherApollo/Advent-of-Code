from copy import deepcopy

with open("./2025/data/4.txt", 'r') as file:
    data = file.readlines()
    data = [x.strip("\n") for x in data]
    data = [list(x) for x in data]
    
class Grid():
    def __init__(self, diagram):
        self.diagram = diagram
        self.markedDiagram = deepcopy(diagram)
        self.maxRows = len(self.diagram)
        self.maxCols = len(self.diagram[0])
        
    def __repr__(self):
        string = "\n"
        for row in self.markedDiagram:
            # string += "".join(row) + "\n"
            string+= str(row) +"\n"
        return string
    
    def validGrid(self, row, col):
        valid = True
        if row < 0 or row >= self.maxRows:
            valid = False
        if col < 0 or col >= self.maxCols:
            valid = False
        return valid

    def getNeighbors(self, row, col):
        neighbor_coords = [
            (row + 1, col -1),
            (row, col -1),
            (row -1, col -1),
            (row + 1, col),
            (row -1, col),
            (row + 1, col +1),
            (row, col +1),
            (row -1, col +1),
        ]
        # Filtering out invalid cords
        neighbors = []
        for row, col in neighbor_coords:
            if self.validGrid(row, col):
                neighbors.append(self.diagram[row][col])
        
        return neighbors
    
    def part1(self, row, col):
        valid = False
        neighbors = self.getNeighbors(row, col)
        if self.diagram[row][col] != "@":
            return valid
        
        rolls = 0
        for x in neighbors:
            if x == "@":
                rolls += 1
                
        if rolls < 4:
            valid = True
            self.markedDiagram[row][col] = "X"
            
        return valid
    
    def getAccessible(self):
        accessible = 0
        for i in range(self.maxRows):
            for j in range(self.maxCols):
                # print(i,j)
                if self.part1(i,j):
                    accessible += 1
        return accessible
    
    def cleanup(self):
        for i in range(self.maxRows):
            for j in range(self.maxCols):
                if self.markedDiagram[i][j] == "X":
                    self.diagram[i][j] = "."
                    
        self.markedDiagram = deepcopy(self.diagram)
        

def testPartOne():
    lines = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")
    test = []
    for line in lines:
        test.append([x for x in line.strip()])
    
    grid = Grid(test)
    
    print(grid.getNeighbors(0,8))
    print(grid.getNeighbors(0,0))
    print(grid.diagram[1][7])
    
    accessible = 0
    for i in range(grid.maxRows):
        for j in range(grid.maxCols):
            # print(i,j)
            if grid.part1(i,j):
                accessible += 1
    print(grid)
    
    
testPartOne()


grid = Grid(data)
accessible = 0
for i in range(grid.maxRows):
    for j in range(grid.maxCols):
        # print(i,j)
        if grid.part1(i,j):
            accessible += 1
print(f"Part One: {accessible}")

def testPartTwo():
    lines = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")
    test = []
    for line in lines:
        test.append([x for x in line.strip()])
    
    grid = Grid(test)
    print(grid)
    
    print(grid.getNeighbors(0,8))
    print(grid.getNeighbors(0,0))
    print(grid.diagram[1][7])
    
    removed = 0
    while grid.getAccessible() > 0:
        accessible = grid.getAccessible()
        removed += accessible
        grid.cleanup()
    
    print(removed)
    
    if removed != 43:
        raise ValueError(f"Failed test with {removed}")
    
testPartTwo()

grid = Grid(data)
removed = 0
while grid.getAccessible() > 0:
    accessible = grid.getAccessible()
    removed += accessible
    grid.cleanup()

print(removed)
print(f"Part Two: {removed}")