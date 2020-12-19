def read_input():
    file = open('input.txt')
    puzzle_input = [line.replace('mem', '').replace('[', '').replace(']', '').split(' = ') for line in file.readlines()]
    file.close()
    return puzzle_input


def part1(puzzle_input):
    mask_0, mask_1 = 0, 0
    memory = {}
    for i, v in puzzle_input:
        if i == 'mask':
            mask_0 = int(v.replace('X', '1'), 2)
            mask_1 = int(v.replace('X', '0'), 2)
        else:
            addr, v = int(i), int(v)
            memory[addr] = v & mask_0 | mask_1
    return sum(memory.values())


def part2(puzzle_input):
    mask = ''
    memory = {}
    for i, v in puzzle_input:
        if i == 'mask':
            mask = v
        else:
            addr = bin(int(i))[2:].zfill(36)
            addr = [bit_mask if bit_mask in '1X' else bit_address for bit_address, bit_mask in zip(addr, mask)]
            xs = [i for i, bit in enumerate(addr) if bit == 'X']
            for comb in range(1 << len(xs)):
                for k, bit in enumerate(bin(comb)[2:].zfill(len(xs))):
                    addr[xs[k]] = bit
                memory[''.join(addr)] = int(v)
    return sum(memory.values())


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #9628746976360
    print('Part 2: ' + str(part2(puzzle_input))) #4574598714592


if __name__ == '__main__':
    main()
