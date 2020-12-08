import time
from itertools import combinations


def read_input():
    file = open('input.txt')
    result = [int(line) for line in file]
    file.close()
    return result


def determine_two_values(puzzle_input):
    for i, j in combinations(puzzle_input, 2):
        if i + j == 2020:
            return i, j


def determine_tree_values(puzzle_input):
    for i, j, k in combinations(puzzle_input, 3):
        if i + j + k == 2020:
            return i, j, k


def main():
    puzzle_input = read_input()
    values = determine_two_values(puzzle_input)
    print('Part 1: ' + str(values[0] * values[1]))  # 16, 2004 -> 32064

    values = determine_tree_values(puzzle_input)
    print('Part 2: ' + str(values[0] * values[1] * values[2]))  # 248, 820, 952 -> 193598720


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s ms ---" % ((time.time() - start_time) * 1000))
