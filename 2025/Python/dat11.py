from collections import deque

test = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".split("\n")
print(test)

part2test = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".splitlines()

with open("Advent-of-Code/2025/data/11.txt", 'r') as file:
    data = file.read().split("\n")

mapping = {}
for line in data:
    key, value = [x.strip() for x in line.split(":")]
    value = [x.strip() for x in value.split(" ")]
    mapping[key] = value

testMapping = {}
for line in part2test:
    key, value = [x.strip() for x in line.split(":")]
    value = [x.strip() for x in value.split(" ")]
    testMapping[key] = value

def partOne(mapping):
    start = "you"
    stop = "out"

    queue = deque([start])
    visited = {}
    paths = 0

    while queue:
        current = queue.popleft()
        
        for neighbor in mapping[current]:
            if neighbor == "out":
                paths += 1
                continue
            # if neighbor not in visited:
            #     queue.append(neighbor)
            #     visited[neighbor] = True
            
            if neighbor in mapping:
                queue.append(neighbor)
    return paths

def checkPath(path, required):
    if path[-1] != "out":
        return False
    for node in required:
        if node not in path:
            return False
            
    return True

def partTwo(current:str, path:list, visited:set, required:list, mapping:dict):
    # Base Case
    if current == "out":
        if all(node in path for node in required):
            return 1
        return 0
    
    # prevent revisits within a path
    if current in visited:
        return 0
    if current not in mapping:
        return 0
    
    # recursion bit
    total = 0
    visited.add(current)
    for neighbor in mapping.get(current):
        total += partTwo(
            current=neighbor,
            path=path + [current],
            visited=visited, 
            required=required,
            mapping=mapping
        )
    # Backtracking
    visited.remove(current)
    return total
    
print(f"Part One: {partOne(mapping)}")
partTwoResult = partTwo(
    current="svr",
    path=[],
    visited=set(),
    required=["dac", "fft"],
    mapping=mapping
)
print(f"Part Two: {partTwoResult}")

