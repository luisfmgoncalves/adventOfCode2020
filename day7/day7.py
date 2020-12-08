import re


def read_input():
    file = open('input.txt')
    puzzle_input = {}
    for line in file:
        bag, items = re.match('(\\w+ \\w+) bags contain (.*)', line).groups()
        puzzle_input[bag] = [[int(i.group(1)), i.group(2)] for i in re.finditer('(\\d+) (\\w+ \\w+) bags?', items)]
    file.close()
    return puzzle_input


def contains(bag, puzzle_input):
    for b in puzzle_input[bag]:
        if b[1] == "shiny gold" or contains(b[1], puzzle_input):
            return True

    return False


def part1(puzzle_input):
    count = 0
    for bag in puzzle_input.keys():
        if contains(bag, puzzle_input):
            count += 1
    return count


def contained(bag, puzzle_input):
    count = 0
    for b in puzzle_input[bag]:
        count += (b[0] * (1 + contained(b[1], puzzle_input)))
    return count


def part2(puzzle_input):
    return contained("shiny gold", puzzle_input)


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #128
    print('Part 2: ' + str(part2(puzzle_input))) #20189


if __name__ == "__main__":
    main()