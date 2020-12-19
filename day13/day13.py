import re
import math


def read_input():
    file = open('input.txt')
    timestamp = int(file.readline())
    line = file.readline()
    busses = [int(s) for s in line.split(',') if s.isdigit()]
    file.close()
    return timestamp, busses


def sort_buses(t):
    return t[1]


def part1(timestamp, busses):
    b = []
    for bus in busses:
        b.append((bus, math.ceil(timestamp/bus) * bus))
    b = sorted(b, key=sort_buses)
    for t in b:
        if t[1] >= timestamp:
            print(str((t[1] - timestamp) * t[0]))
            break


def part2(timestamp, busses):
    #TODO:
    return 0


def main():
    timestamp, busses = read_input()
    print('Part 1: ' + str(part1(timestamp, busses))) #1895
    print('Part 2: ' + str(part2(timestamp, busses))) #?


if __name__ == '__main__':
    main()
