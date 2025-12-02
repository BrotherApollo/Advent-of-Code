with open("./2025/data/2.txt", 'r') as file:
    data = file.readlines()[0].split(',')
    
print(data)



def find_invalid(start, stop):
    invalid = []
    for i in range(start, stop+1, 1):
        numStr = str(i)
        length = len(numStr)
        
        # # Part 1
        # if numStr[:length//2] == numStr[length//2:]:
        #     invalid.append(i)
            
        # Part 2
        for size in range(1, length):
            if length % size != 0: continue
            
            repetitions = length // size
            if repetitions >= 2:
                pattern = numStr[:size] * repetitions
                
                if pattern == numStr:
                    invalid.append(i)
                    break

    return invalid


# Testing
testMap = [
    {"start": 11, "stop":22, "answer": [11, 22]},
    {"start": 998, "stop":1012, "answer": [999, 1010]},
    {"start": 2121212118, "stop":2121212124, "answer": [2121212121]},
]

for test in testMap:
    answer = find_invalid(test["start"], test["stop"])
    if answer != test["answer"]:
        raise ValueError(f"filed test {test} with {answer}")
    
    print(f"{test} : {answer}")
    
print("Passed all Test cases")

bad_ids = []

for idRange in data:
    start, stop = [int(x) for x in idRange.split("-")]
    bad_ids.extend(find_invalid(start, stop))
    
print(sum(bad_ids))



