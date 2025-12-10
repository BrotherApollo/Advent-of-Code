test = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

class Machine():
    def __init__(self, rawdata):
        self.rawdata = rawdata
        self.formatData()
        # Setting values for building Matrix
        self.numLights = len(self.target)
        self.numButtons = len(self.buttons)
        
    def formatData(self):
        data = self.rawdata.split(" ")
        # Formating Target
        self.target = [x for x in data[0].strip("[]")]
        # Formating Joltage
        self.joltage = data[-1].strip("{}").split(",")
        # Formating Buttons
        self.buttons = []
        for button in data[1:-1]:
            new_button = [int(x) for x in button.strip("()").split(",")]
            self.buttons.append(new_button)
        
        

data = test.split(" ")
print(data)
bot = Machine(test)

lightMatrix = []
for light_index in range(bot.numLights):
    row = [0] * (bot.numButtons + 1)
    for button_index, button in enumerate(bot.buttons):
        if light_index in button:
            row[button_index] = 1
            
    row[-1] = bot.target[light_index]
    lightMatrix.append(row)
        
for row in lightMatrix:
    print(row)
print(bot.__dict__)