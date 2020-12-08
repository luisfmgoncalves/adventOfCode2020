def read_input():
    file = open('input.txt')
    puzzle_input = [line.split('\n\n') for line in file]
    file.close()
    return format_input(puzzle_input)


def format_input(puzzle_input):
    result = []
    current = ''
    for e in puzzle_input:
        if e[0] == '\n':
            result.append(current.strip())
            current = ''
        else:
            current = current + ' ' + str(e[0].replace('\n',''))
            if puzzle_input[-1] == e:
                result.append(current.strip())
    return result


def part1(puzzle_input):
    return sum([len("".join(set(s.replace(' ','')))) for s in puzzle_input])


def part2(puzzle_input):
    temp_hash = {}
    count = 0
    for group in puzzle_input:
        parts = group.split()
        for p in parts:
            for char in p:
                if char in temp_hash:
                    temp_hash[char] += 1
                else:
                    temp_hash[char] = 1

            for k, v in temp_hash.items():
                if v == len(parts):
                    count += 1
        temp_hash = {}
    return count


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #6521
    print('Part 2: ' + str(part2(puzzle_input))) #3305


if __name__ == '__main__':
    main()