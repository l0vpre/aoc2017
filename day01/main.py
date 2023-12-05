import sys

def part1(filepath):
    with open(filepath,'r') as file:
        file = file.read().strip("\n")
        sum = 0
        for i in range(len(file)-1):
            if file[i] == file[i+1]:
                sum += int(file[i])
        if file[len(file)-1] == file[0]:
            sum+= int(file[len(file)-1])
    return sum


def part2(filepath):
    with open(filepath,'r') as file:
        file = file.read().strip("\n")
        diff = int(len(file)/2)
        sum = 0
        
        for i in range(len(file)):
            next = i + diff
            if next >= len(file):
                next -= len(file)
            if file[i] == file[next]:
                sum += int(file[i])
    return sum
    

if __name__ == "__main__":
    for file in sys.argv[1:]:
        print(f'Solving {file}')
        print(f'Part 1: {part1(file)}')
        print(f'Part 2: {part2(file)}')

