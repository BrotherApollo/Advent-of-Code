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

# class Dial(): 
    
#     def __init__(self):
#         self.value = 50
#         self.zeros = 0
        
#     def __add__(self, value): 
#         self.value += value
#         while self.value > 99:
#             self.value -= 100
#             self.zeros += 1
            
#     def __sub__(self, value):
#         self.value -= value
#         while self.value < 0:
#             self.value += 100
#             self.zeros += 1

# class Dial(): 
    
#     def __init__(self):
#         self.value = 50
#         self.zeros = 0
        
#     def turn(self, direction, value):
#         fullturns = value // 100
#         print(f"ripping {fullturns}")
#         self.zeros += fullturns
        
#         change = value % 100
#         print(f"changing {change}")
        
#         if direction == "L":
#             self.value -= change
#         elif direction == "R":
#             self.value += change

#         if self.value > 0 and self.value < 100:
#             return
        
#         if self.value != 0:
#             print("plus one")
#             self.zeros += 1
        
#         if self.value < 0:
#             self.value += 100
            
#         elif self.value > 99:
#             self.value -= 100
            
#         print(self.value)

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
