import sys

def part1(filepath):
    def get_dif(line: str) -> int:
        line = line.replace('\t', ' ')
        line = line.split(' ')
        line = filter(lambda l: l  != "  " or '   ', line)
        line = list(map(int,line))
        return max(line) - min(line)


    with open(filepath) as file:
        lines = file.readlines()
        return sum(map(get_dif, lines))
    


def part2(filepath):
    def get_dif(line: str) -> int:
        line = line.replace('\t', ' ')
        line = line.split(' ')
        line = filter(lambda l: l  != "", line)
        line = list(map(int,line))
        divis = 0
        for i in range(len(line)):
            for g in range(len(line)):
                if g == i:
                    continue
                if line[i] % line[g]==0:
                    divis = line[i] // line[g]
        return divis
     
    with open(filepath) as file:
        lines = file.readlines()
        return sum(map(get_dif, lines))

if __name__ == "__main__":
    for file in sys.argv[1:]:
        print(f'Solving {file}')
        print(f'Part 1: {part1(file)}')
        print(f'Part 2: {part2(file)}')
