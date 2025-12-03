with open("./2025/data/3.txt", 'r') as file:
    data = file.readlines()
    data = [x.strip("\n") for x in data]


# Part one
def max_jolt(batteries:str) -> int:
    
    first = max(batteries[:-1])
    first_index = batteries.index(first)
    second = max(batteries[first_index+1:])
    
    return int(f"{first}{second}")
    
jolts = []
for line in data:
    jolts.append(max_jolt(line))
    
print(f"Part one: {sum(jolts)}")

# Part two

tests = [
    {"input": "987654321111111", "answer": 987654321111},
    {"input": "811111111111119", "answer": 811111111119},
    {"input": "234234234234278", "answer": 434234234278},
    {"input": "818181911112111", "answer": 888911112111},
]
test_total = 3121910778619

# def part2(line):
#     jolt = [int(x) for x in line[-12:]]
#     remaining = line[:-12]
#     for i in remaining[::-1]:
#         hold = int(i)
#         for index, digit in enumerate(jolt):
#             if hold > digit:
#                 jolt[index] = hold
#                 hold = digit
#     return int("".join([str(x) for x in jolt]))

def part2(line):
    # print(line)
    to_select = 12
    length = len(line)
    jolts = []
    start = 0
    for pos in range(to_select):
        remaining_selections = to_select - pos - 1
        stop = length - remaining_selections
        
        max_num = max(line[start:stop])
        max_index = line.index(max_num, start, stop)
                
        start = max_index + 1
        jolts.append(max_num)
        
    return int("".join([str(x) for x in jolts]))
        

for test in tests:
    value = part2(test.get("input"))
    if value != test.get("answer"):
        print("Failed test")
        print(value, test.get("answer"))
        
        
        
jolts = []
for line in data:
    jolts.append(part2(line))
    
print(f"Part two: {sum(jolts)}")