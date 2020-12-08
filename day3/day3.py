import time


def read_input():
    file = open('input.txt')
    lines = [line.rstrip() for line in file]
    file.close()
    return lines


def part1():
    lines = read_input()
    col = 0
    num_trees = 0
    for line in lines:
        l = len(line)
        if col >= l:
            col -= l
        if line[col] == '#':
            num_trees += 1
        col += 3

    return num_trees


def has_tree(line, col):
    return True if line[col] == '#' else False


#It looks horrible, I know!
def part2():
    lines = read_input()
    #results
    res_a, res_b, res_c, res_d, res_e = 0, 0, 0, 0, 0
    #columns
    col_a, col_b, col_c, col_d, col_e = 0, 0, 0, 0, 0

    for line in lines:
        l = len(line)
        if col_a >= l:
            col_a -= l
        if col_b >= l:
            col_b -= l
        if col_c >= l:
            col_c -= l
        if col_d >= l:
            col_d -= l
        if col_e >= l:
            col_e -= l

        if has_tree(line, col_a):
            res_a += 1
        if has_tree(line, col_b):
            res_b += 1
        if has_tree(line, col_c):
            res_c += 1
        if has_tree(line, col_d):
            res_d += 1
        if lines.index(line) % 2 == 0 and has_tree(line, col_e):
            res_e += 1

        col_a += 1
        col_b += 3
        col_c += 5
        col_d += 7
        if lines.index(line) % 2 == 0:
            col_e += 1

    return res_a * res_b * res_c * res_d * res_e


def main():
    print('Part 1: ' + str(part1())) #252
    print('Part 2: ' + str(part2())) #2608962048


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s ms ---" % ((time.time() - start_time) * 1000))
