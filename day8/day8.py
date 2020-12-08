import re


def read_input():
    file = open('input.txt')
    puzzle_input = []
    for line in file:
        m = re.search('^(\\w+)\\s([+,-])(\\d+)$', line)
        if m:
            puzzle_input.append((m.group(1), m.group(2), int(m.group(3))))
    file.close()
    return puzzle_input


def execute_operation(state, action):
    op = action[0]
    index = state[0]
    acc = state[1]

    if op == 'nop':
        index += 1
    elif op == 'acc':
        acc = acc + action[2] if action[1] == '+' else acc - action[2]
        index += 1
    elif op == 'jmp':
        index = index + action[2] if action[1] == '+' else index - action[2]
    return index, acc


def part1(puzzle_input):
    visited_indices = []
    state = (0, 0) #index, acc
    while state[0] not in visited_indices:
        i = state[0]
        state = execute_operation(state, puzzle_input[i])
        visited_indices.append(i)
    return state[1]


#brute force solution: change every `jmp` and `nop` and check if we reach the end of the input
#TODO: refactor!
def part2(puzzle_input):
    for entry in puzzle_input:
        op = entry[0]
        if op == 'acc': continue
        new_entry = ('jmp', entry[1], entry[2]) if entry[0] == 'nop' else ('nop', entry[1], entry[2]) #swap operation
        i = puzzle_input.index(entry)
        input_to_verify = puzzle_input[:i] + [new_entry] + puzzle_input[(i + 1):]

        visited_indices = []
        state = (0, 0) #index, acc
        while state[0] not in visited_indices:
            if state[0] >= len(input_to_verify):
                return state[1] #found!
            i = state[0]
            state = execute_operation(state, input_to_verify[i])
            visited_indices.append(i)


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #1262
    print('Part 2: ' + str(part2(puzzle_input))) #1643


if __name__ == '__main__':
    main()
