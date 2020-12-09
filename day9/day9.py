PREAMBLE = 5


def read_input():
    file = open('input.txt')
    puzzle_input = [int(line) for line in file]
    file.close()
    return puzzle_input


def part1(puzzle_input):
    lower_bound = 0
    upper_bound = lower_bound + PREAMBLE
    while upper_bound < len(puzzle_input) - 2:
        sublist = puzzle_input[lower_bound:upper_bound]
        to_find = puzzle_input[upper_bound]
        found = False
        for i in sublist:
            for j in sublist:
                if i != j and i + j == to_find:
                    found = True
                    break
            if found: break

        if not found: return to_find
        lower_bound += 1
        upper_bound += 1


def part2(to_find, puzzle_input):
    lower_bound = 0
    upper_bound = 0
    while upper_bound < len(puzzle_input):
        current_sublist = puzzle_input[lower_bound:upper_bound]
        current_sum = sum(current_sublist)
        if current_sum == to_find:
            print(current_sublist)
            current_sublist.sort()
            return current_sublist[0] + current_sublist[-1]
        elif upper_bound < len(puzzle_input) - 1:
            upper_bound += 1
        else:
            lower_bound += 1
            upper_bound = lower_bound


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #32321523
    print('Part 2: ' + str(part2(32321523, puzzle_input)))#4794981


if __name__ == '__main__':
    main()