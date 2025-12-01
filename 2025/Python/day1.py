with open("./2025/data/1.txt", 'r') as file:
    data = [x.strip("\n") for x in file if x]
    
print(data)


test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")

class Dial(): 
    
    def __init__(self):
        self.value = 50
        self.zeros = 0
        
    def turn(self, direction, value):
        
        for i in range(value):
            if direction == "L":    
                self.value = (self.value - 1) % 100
            else: 
                self.value = (self.value + 1) % 100
                
            if self.value == 0:
                self.zeros += 1 

dial = Dial()
        
for t in data:
    direction, value = (t[0], int(t[1:]))
    print(direction, value)
    
    dial.turn(direction, value)
    
    # if dial.value == 0:
    #     dial.zeros += 1
    # print(dial.value)
    
print(dial.zeros)
