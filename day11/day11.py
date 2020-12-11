def read_input():
    file = open('input.txt')
    puzzle_input = [line.replace('\n', '') for line in file]
    file.close()
    return puzzle_input


def change_seat(seat, adjacent, limit):
    if seat == 'L' and '#' not in adjacent:
        return '#'
    if seat == '#' and adjacent.count('#') >= limit:
        return 'L'
    return seat


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def find_adjacent_part1(row, col, puzzle_input):
    adjacent = []
    for d in directions:
        curr = [row + d[0], col + d[1]]
        if (0 <= curr[0] < len(puzzle_input)) and (0 <= curr[1] < len(puzzle_input[row])):
            seat = puzzle_input[curr[0]][curr[1]]
            if seat != '.':
                adjacent.append(seat)
    return adjacent


def find_adjacent_part2(row, col, puzzle_input):
    adjacent = []
    for d in directions:
        curr = [row + d[0], col + d[1]]
        found = False
        while (0 <= curr[0] < len(puzzle_input)) and (0 <= curr[1] < len(puzzle_input[row])) and not found:
            seat = puzzle_input[curr[0]][curr[1]]
            if seat != '.':
                found = True
                adjacent.append(seat)
            else:
                curr[0] += d[0]
                curr[1] += d[1]
    return adjacent


def run(puzzle_input, part):
    previous = puzzle_input[:]
    sited = 0
    while True:
        result = previous[:]
        for row in range(0, len(previous)):
            seat_row = ''
            for col in range(0, len(previous[row])):
                seat = previous[row][col]
                if seat != '.':
                    #most likely there is a better way to do this
                    if part == 1:
                        adjacent = find_adjacent_part1(row, col, previous)
                        seat = change_seat(seat, adjacent, 4)
                    else:
                        adjacent = find_adjacent_part2(row, col, previous)
                        seat = change_seat(seat, adjacent, 5)
                seat_row += seat
            result[row] = seat_row

        if previous == result: #found the exact same as the starting point. Stop
            for row in result:
                sited += row.count('#')
            break
        else:
            previous = result

    return sited


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(run(puzzle_input, 1))) #2283
    print('Part 2: ' + str(run(puzzle_input, 2))) #2054


if __name__ == '__main__':
    main()
