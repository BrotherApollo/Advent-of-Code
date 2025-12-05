with open("./2025/data/5.txt", 'r') as file:
    data = file.read()
    # print(data)

def splitData(data:str) -> dict:
    data = data.split("\n")

    ranges = []
    ingredients = []

    runningRanges = True
    for line in data:
        line = line.strip()
        if line == "":
            runningRanges = False
        elif runningRanges:
            rMin, rMax = [int(x) for x in line.split("-")]
            ranges.append({"min":rMin, "max": rMax})
        else:
            ingredients.append(int(line))

    return dict(ranges=ranges, ingredients=ingredients)

def sortMergeRanges(ranges: list[dict]):
    ranges = sorted(ranges, key=lambda x: x.get("min"))
    
    merged_ranges = []
    current_range = ranges[0]
    for r in ranges:
        # Not a match to current range
        if r["min"] > current_range["max"]:
            merged_ranges.append(current_range)
            current_range = r
        # Joining
        else:
            current_range["max"] = max(current_range["max"], r["max"])
    merged_ranges.append(current_range)

    # print(ranges)
    return merged_ranges

def runTests():
    test = """3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32"""
    test = splitData(test)


    print(test)
    ranges = sortMergeRanges(test.get("ranges"))
    fresh = 0
    for ingredient in test.get("ingredients"):
        print(ingredient)
        for r in ranges:
            if (ingredient >= r["min"]) and (ingredient <= r["max"]):
                fresh += 1
                break
    if fresh !=3:
        raise ValueError(f"Test Failed expected 3 got {fresh}")
    # print(fresh)

    fresh_ids = 0

    for r in ranges:
        fresh_ids += (r["max"] - r["min"])+1

    print(f"Part Two test: {fresh_ids}")

    
runTests()

# Part One

data = splitData(data)
ranges = sortMergeRanges(data.get("ranges"))
fresh = 0
for ingredient in data.get("ingredients"):
    for r in ranges:
        if (ingredient >= r["min"]) and (ingredient <= r["max"]):
            fresh += 1
            break
print(f"part one: {fresh}")


# Part Two

fresh_ids = 0

for r in ranges:
    fresh_ids += (r["max"] - r["min"])+1

print(f"Part Two: {fresh_ids}")