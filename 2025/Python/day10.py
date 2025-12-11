from itertools import product
from collections import deque

class Machine():
    def __init__(self, rawdata):
        self.rawdata = rawdata
        self.formatData()
        # Setting values for building Matrix
        self.numLights = len(self.target)
        self.numButtons = len(self.buttons)
        self.numJolts = len(self.joltage)
        self.pressedOne = float("inf")
        self.pressedTwo = float("inf")
        
    def formatData(self):
        data = self.rawdata.split(" ")
        # Formating Target
        self.target = [x=="#" for x in data[0].strip("[]")]
        # Formating Joltage
        self.joltage = [int(x) for x in data[-1].strip("{}").split(",")]
        # Formating Buttons
        self.buttons = []
        for button in data[1:-1]:
            new_button = [int(x) for x in button.strip("()").split(",")]
            self.buttons.append(new_button)
            
    def solve(self):
        for combo in product([0,1], repeat=self.numButtons):            
            lights = [0] * self.numLights
            presses = sum(combo)
            
            for index, pressed in enumerate(combo):
                if pressed:
                    for light in self.buttons[index]:
                        lights[light] ^= 1 #XOR opperator homie
                        
            if lights == self.target:
                self.pressedOne = min(self.pressedOne, presses)
    
    def partTwo(self):        
        queue = deque([(tuple([0]*self.numJolts), 0)])  # (state, presses)
        visited = {tuple([0]*self.numJolts): 0}
        
        while queue:
            current, presses = queue.popleft()
            
            # Base Case
            if list(current) == self.joltage:
                return presses
            
            for button_index in range(len(self.buttons)):
                newPath = list(current)
                for jolt_index in self.buttons[button_index]:
                    newPath[jolt_index] += 1
                    
                if any([newPath[i] > self.joltage[i] for i in range(len(newPath))]):
                    continue
                
                newState = tuple(newPath)
                if newState not in visited or visited[newState] > presses + 1:
                    visited[newState] = presses + 1
                    queue.append((newState, presses + 1))
        
        return float("inf")

# Data Prep Machine Object init
tests = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
tbots = [Machine(test) for test in tests.split("\n")]
    
with open("Advent-of-Code/2025/data/10.txt", 'r') as file:
    data = file.read().split("\n")
    # print(data)
bots = [Machine(rawdata) for rawdata in data]

# Part One
for bot in bots:
    # print(bot.__dict__)
    bot.solve()
    bot.pressedTwo = bot.partTwo()
    print(f"{bot.joltage} -> {bot.pressedTwo}")
    
    
print(f"Part One: {sum([x.pressedOne for x in bots])}")
print(f"Part Two: {sum([x.pressedTwo for x in bots])}")

# part_two_results = []
# for bot in tbots:
#     bot.pressedTwo = bot.partTwo()
#     print(f"{bot.joltage} -> {bot.pressedTwo}")
#     part_two_results.append(bot.pressedTwo)
    
# print(f"Part Two: {sum(part_two_results)}")