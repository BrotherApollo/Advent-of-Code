import math
import re

with open("./2025/data/6.txt", 'r') as file:
    data = file.read()
    
    # print(data)
    
def getTestData():
    return """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

def organizeData(data: str) -> dict:
    rows = []
    for row in data.split("\n"):
        rows.append([x for x in row.split(" ") if x])
    result = []
    for i in range(len(rows[0])):
        result.append([x[i] for x in rows])
        
    return result

def part1(data):
    totals = []
    for row in data:
        nums = [int(x) for x in row[:-1]]
        if row[-1] == "*":
            totals.append(math.prod(nums))
        else:
            totals.append(sum(nums))
    return sum(totals)
    
def Part1Test(): 
    testdata = organizeData(getTestData())
    total = part1(testdata)
    assert total == 4277556
    
Part1Test()
    
# Part one
partone = part1(organizeData(data))
print(f"Part one: {partone}")


# Part two
class Problem():
    def __init__(self, nums, sign, step):
        self.nums = nums
        self.sign = sign
        self.step = step
        self.flipped = self.flip()
        self.value = self.total()
        
    def flip(self):
        nums = []
        for i in range(self.step):
            nums.append(int("".join([x[i] for x in self.nums])))
        return nums
    
    def total(self):
        if self.sign == "*":
            return math.prod(self.flipped)
        else:
            return sum(self.flipped)
        
rows = data.split("\n")
steps = []
for item in rows[-1].split("*"):
    steps.extend(item.split("+"))
steps = [len(x) for x in steps if x]
steps[-1] += 1
# print(steps)
result = []
# print(rows)
index = 0
for i in steps:
    result.append([row[index:index+i] for row in rows[:-1]])
    index += i+1
# print(result)
signs = re.findall(r"[*+]{1}", rows[-1])
# for i in range(len(signs)):
#     result[i].append(signs[i])
    
problems = [Problem(
    nums = result[i],
    sign = signs[i],
    step = steps[i]
)for i in range(len(steps))]

print(problems[0].__dict__)
print(problems[0].flip())

print(f"Part Two: {sum([p.value for p in problems])}")

    