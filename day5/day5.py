import math


def read_input():
    file = open('input.txt')
    puzzle_input = [line.strip() for line in file]
    file.close()
    return puzzle_input


def interval(tuple, char):
    lower, upper = tuple[0], tuple[1]
    middle = (upper - lower) / 2
    b = math.floor(upper - middle) if char == 'F' or char == 'L' else upper
    a = math.ceil(lower + middle) if char == 'B' or char == 'R' else lower
    return a, b


def seat_id(line):
    row = (0, 127)
    col = (0, 7)
    for char in line[:7]: row = interval(row, char)
    for char in line[-3:]: col = interval(col, char)
    return (row[0] * 8) + col[0]


def find_missing_seat(seat_list):
    return [s for s in range(seat_list[0], seat_list[-1] + 1) if s not in seat_list]


def main():
    puzzle_input = read_input()
    ids = [seat_id(s) for s in puzzle_input]
    ids.sort()

    print('Part 1: ' + str(ids[-1]))#850
    print('Part 2: ' + str(find_missing_seat(ids)[0]))#599


if __name__ == '__main__':
    main()