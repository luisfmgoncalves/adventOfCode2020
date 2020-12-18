def read_input():
    file = open('input.txt')
    puzzle_input = [int(x) for x in file.readline().split(',')]
    file.close()
    return puzzle_input


def part1(puzzle_input, th):
    numbers = {}
    turn = 1
    spoken = []
    for i in puzzle_input:
        add_number(i, turn, numbers)
        spoken.append(i)
        turn += 1

    while turn <= th:
        last = spoken[-1]
        if last not in numbers.keys() or len(numbers[last]) == 1:
            add_number(0, turn, numbers)
            spoken.append(0)
        else:
            l = numbers[last]
            x = l[-1] - l[-2]
            spoken.append(x)
            add_number(x, turn, numbers)
        turn += 1

    return spoken[-1]


def add_number(i, turn, numbers):
    if i in numbers:
        numbers[i].append(turn)
    else:
        numbers[i] = [turn]


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input, 2020))) #870
    print('Part 2: ' + str(part1(puzzle_input, 30000000))) #9136


if __name__ == '__main__':
    main()
