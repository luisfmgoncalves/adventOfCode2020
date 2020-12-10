def read_input():
    file = open('input.txt')
    puzzle_input = [int(line) for line in file]
    puzzle_input.sort()
    puzzle_input = [0] + puzzle_input + [(puzzle_input[-1] + 3)]  # adds the charging outlet and device built-in adapter
    file.close()
    return puzzle_input


def part1(puzzle_input):
    current = 0
    differences = []
    for i in puzzle_input:
        diff = i - current
        if diff <= 3:
            differences.append(diff)
        current = i
    return differences.count(1) * differences.count(3)


#(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#> 1, 1, 1, 1, 2, 4, 4, 4, 8, 8, 8, 8,
#(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
#> 1, 1, 1, 1, 2, 4, 4, 4, 8, 8, 8, 8,
#(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
#> 1, 1, 1, 1, 2, 2,  2, 4, 4, 4, 4
#(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)

#sum of the previous 3 elements if they're in the range of 3
#sure some positions can be reached in less steps but those are ignored
def part2(puzzle_input):
    #stores the highest value per index
    positions = [1] + [0 for n in range(0, len(puzzle_input) - 1)]
    for i in range(0, len(puzzle_input)):
        for j in range(i - 3, i):
            if j < 0:
                continue
            if puzzle_input[i] - puzzle_input[j] <= 3:
                positions[i] += positions[j]
                #print(positions)
    return positions[-1]


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #1876
    print('Part 2: ' + str(part2(puzzle_input))) #14173478093824


if __name__ == '__main__':
    main()
