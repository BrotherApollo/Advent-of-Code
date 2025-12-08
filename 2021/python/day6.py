from collections import defaultdict

with open("Advent-of-Code/2021/data/6.txt", 'r') as file:
    data = file.read()

data = [int(x) for x in data.split(",")]

Fish = defaultdict(int)

for item in data:
    Fish[item] += 1
    
def nextDay(dict):
    newDict = defaultdict(int)

    for day, count in dict.items():
        nextday = day - 1
        if nextday < 0:
            newDict[8] += count
            newDict[6] += count
        else:
            newDict[nextday] += count
            
    return newDict

for i in range(256):
    day = i + 1
    Fish = nextDay(Fish)
    if day == 80:
        print(f"Part One: {sum(Fish.values())}")
    if day == 256:
        print(f"Part Two: {sum(Fish.values())}")