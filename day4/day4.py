import time
import re


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


def is_valid_passport_part1(p):
    has_byr = re.search('(^|\\s)byr:(.*)(\\s|$)', p)
    has_iyr = re.search('(^|\\s)iyr:(.*)(\\s|$)', p)
    has_eyr = re.search('(^|\\s)eyr:(.*)(\\s|$)', p)
    has_hgt = re.search('(^|\\s)hgt:(.*)(\\s|$)', p)
    has_hcl = re.search('(^|\\s)hcl:(.*)(\\s|$)', p)
    has_ecl = re.search('(^|\\s)ecl:(.*)(\\s|$)', p)
    has_pid = re.search('(^|\\s)pid:(.*)(\\s|$)', p)

    return has_byr and has_iyr and has_eyr and has_hgt and has_hcl and has_ecl and has_pid


def part1(puzzle_input):
    count = 0
    for entry in puzzle_input:
        if is_valid_passport_part1(entry):
            count += 1
    return count


def is_valid_passport_part2(p):
    byr = re.search('(^|\\s)byr:(\\d+)(\\s|$)', p)
    valid_byr = byr and 2002 >= int(byr.group(2)) >= 1920

    iyr = re.search('(^|\\s)iyr:(\d+)(\\s|$)', p)
    valid_iyr = iyr and 2020 >= int(iyr.group(2)) >= 2010

    eyr = re.search('(^|\\s)eyr:(\\d+)(\\s|$)', p)
    valid_eyr = eyr and 2030 >= int(eyr.group(2)) >= 2020

    hgt = re.search('(^|\\s)hgt:(\\d+)(cm|in)(\\s|$)', p)
    valid_hgt = False
    if hgt:
        if hgt.group(3) == 'cm':
            valid_hgt = 193 >= int(hgt.group(2)) >= 150
        elif hgt.group(3) == 'in':
            valid_hgt = 76 >= int(hgt.group(2)) >= 59

    hcl = re.search('(^|\\s)hcl:(#[a-f0-9]+)(\\s|$)', p)
    ecl = re.search('(^|\\s)ecl:(amb|blu|brn|gry|grn|hzl|oth)(\\s|$)', p)
    pid = re.search('(^|\\s)pid:(\\d{9})(\\s|$)', p)

    return valid_byr and valid_iyr and valid_eyr and valid_hgt and hcl and ecl and pid


def part2(puzzle_input):
    count = 0
    for entry in puzzle_input:
        if is_valid_passport_part2(entry):
            count += 1
    return count


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #235
    print('Part 2: ' + str(part2(puzzle_input))) #194


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s ms ---" % ((time.time() - start_time) * 1000))