import time
import re


def is_valid_password_part1(min, max, chr, pwd):
    return True if min <= pwd.count(chr) <= max else False


def is_valid_password_part2(min, max, chr, pwd):
    indices = [i for i, letter in enumerate(pwd) if letter == chr]
    has_min = min - 1 in indices and max - 1 not in indices
    has_max = max - 1 in indices and min - 1 not in indices
    return has_min or has_max


def main():
    #iterate through the contents of the file only once
    f = open('input.txt')
    part1_result = 0
    part2_result = 0
    for line in f:
        m = re.search('^(?P<min>\\d+)-(?P<max>\\d+)\\s(?P<chr>\\w):\\s(?P<pwd>\\w+)$', line)
        if is_valid_password_part1(int(m.group('min')), int(m.group('max')), m.group('chr'), m.group('pwd')):
            part1_result += 1
        if is_valid_password_part2(int(m.group('min')), int(m.group('max')), m.group('chr'), m.group('pwd')):
            part2_result += 1
    f.close()

    print('Part 1: ' + str(part1_result)) #628
    print('Part 2: ' + str(part2_result)) #705


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s ms ---" % ((time.time() - start_time) * 1000))
