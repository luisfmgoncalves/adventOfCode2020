def read_input():
    file = open('input.txt')
    puzzle_input = [line.replace('\n', '') for line in file]
    file.close()
    return puzzle_input


NORTH_RIGHT = {90: 'E', 180: 'S', 270: 'W'}
NORTH_LEFT = {90: 'W', 180: 'S', 270: 'E'}
EAST_RIGHT = {90: 'S', 180: 'W', 270: 'N'}
EAST_LEFT = {90: 'N', 180: 'W', 270: 'S'}
SOUTH_RIGHT = {90: 'W', 180: 'N', 270: 'E'}
SOUTH_LEFT = {90: 'E', 180: 'N', 270: 'W'}
WEST_RIGHT = {90: 'N', 180: 'E', 270: 'S'}
WEST_LEFT = {90: 'S', 180: 'E', 270: 'N'}


def move_ship_part_1(action, units, facing, ship):
    if action == "N": ship["N"] += units
    elif action == "S": ship["N"] -= units
    elif action == "E": ship["E"] += units
    elif action == "W": ship["E"] -= units
    elif action == 'F':
        if facing == 'E': ship["E"] += units
        if facing == 'S': ship["N"] -= units
        if facing == 'W': ship["E"] -= units
        if facing == 'N': ship["N"] += units
    elif action == 'L':
        if facing == 'N': facing = NORTH_LEFT[units]
        elif facing == 'E': facing = EAST_LEFT[units]
        elif facing == 'S': facing = SOUTH_LEFT[units]
        else: facing = WEST_LEFT[units]
    elif action == 'R':
        if facing == 'N': facing = NORTH_RIGHT[units]
        elif facing == 'E': facing = EAST_RIGHT[units]
        elif facing == 'S': facing = SOUTH_RIGHT[units]
        else: facing = WEST_RIGHT[units]
    return facing, ship


def part1(puzzle_input):
    ship = {"N": 0, "S": 0, "E": 0, "W": 0}
    facing = 'E'
    for line in puzzle_input:
        action, units = line[0], int(line[1:])
        facing, ship = move_ship_part_1(action, units, facing, ship)
    return abs(ship['E']) + abs(ship['N'])


def move_ship_part_2(action, units, facing, waypoint, ship):
    if action == "N": waypoint["N"] += units
    elif action == "S": waypoint["N"] -= units
    elif action == "E": waypoint["E"] += units
    elif action == "W": waypoint["E"] -= units
    elif action == 'F':
        for x in range(units):
            if facing == 'N':
                ship["E"] -= waypoint["N"]
                ship["N"] -= waypoint["E"]
            if facing == 'S':
                ship["E"] += waypoint["N"]
                ship["N"] += waypoint["E"]
            if facing == 'E':
                ship["E"] += waypoint["E"]
                ship["N"] += waypoint["N"]
            if facing == 'W':
                ship["E"] -= waypoint["E"]
                ship["N"] -= waypoint["N"]
    elif action == 'L':
        if units == 90:
            waypoint["E"], waypoint["N"] = -waypoint["N"], waypoint["E"]
        elif units == 270:
            waypoint["E"], waypoint["N"] = waypoint["N"], -waypoint["E"]
        elif units == 180:
            waypoint["E"] = -waypoint["E"]
            waypoint["N"] = -waypoint["N"]
    elif action == 'R':
        if units == 90:
            waypoint["E"], waypoint["N"] = waypoint["N"], -waypoint["E"]
        elif units == 270:
            waypoint["E"], waypoint["N"] = -waypoint["N"], waypoint["E"]
        elif units == 180:
            waypoint["E"] = -waypoint["E"]
            waypoint["N"] = -waypoint["N"]
    return waypoint, ship


def part2(puzzle_input):
    ship = {"N": 0, "S": 0, "E": 0, "W": 0}
    waypoint = {"N": 1, "S": 0, "E": 10, "W": 0}
    facing = 'E'
    for line in puzzle_input:
        action, units = line[0], int(line[1:])
        waypoint, ship = move_ship_part_2(action, units, facing, waypoint, ship)
    return abs(ship['E']) + abs(ship['N'])


def main():
    puzzle_input = read_input()
    print('Part 1: ' + str(part1(puzzle_input))) #441
    print('Part 2: ' + str(part2(puzzle_input))) #40014


if __name__ == '__main__':
    main()
