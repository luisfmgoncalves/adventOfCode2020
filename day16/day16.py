import re


def read_input():
    file = open('input.txt')
    rules = {}
    tickets = []
    for line in file.readlines():
        line = line.replace('\n', '')
        r = re.search('^([a-z ]+): (\\d+)-(\\d+) or (\\d+)-(\\d+)$', line)
        if r:
            rules[r.group(1)] = [(int(r.group(2)), int(r.group(3))), (int(r.group(4)), int(r.group(5)))]
            continue
        t = re.search('^(\\d+(,\\d+)*)$', line)
        if t:
            tickets.append([int(n) for n in line.split(',')])
    file.close()
    return rules, tickets


def part1(rules, tickets):
    res = 0
    for ticket in tickets[1:]: #first ticket is our own
        for t in ticket:
            found = False
            for rule in rules.values():
                low = rule[0]
                high = rule[1]
                if low[0] <= t <= low[1] or high[0] <= t <= high[1]:
                    found = True
                    break
            if not found:
                res += t
    return res


def get_valid_tickets(rules, tickets):
    res = []
    for ticket in tickets[1:]: #first ticket is our own
        valid = True
        for t in ticket:
            found = False
            for r in rules.values():
                low = r[0]
                high = r[1]
                if low[0] <= t <= low[1] or high[0] <= t <= high[1]:
                    found = True
                    break
            if not found:
                valid = False
                break
        if valid:
            res.append(ticket)
    return res


def part2(rules, tickets):
    own_ticket = tickets[0]
    valid_tickets = get_valid_tickets(rules, tickets)

    if len(valid_tickets) == 0:
        print('There are no valid tickets in that input. Exiting...')
        return

    #each index in a ticket mapped to the fields that are possible for that index
    possible_fields = {i: set(rules.keys()) for i in range(len(valid_tickets[0]))}
    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            for field in rules:
                possible = False
                for lo, hi in rules[field]:
                    if lo <= value <= hi:
                        possible = True
                        break
                if not possible:
                    possible_fields[i].discard(field)

    #remove the indices that only have one possible value
    for i in sorted(possible_fields, key=lambda k: len(possible_fields[k])):
        this_field = next(iter(possible_fields[i]))
        for j in possible_fields:
            if i != j:
                possible_fields[j].discard(this_field)

    result = 1
    for value in possible_fields:
        if possible_fields[value].pop().startswith("departure"):
            result *= own_ticket[value]
    return result


def add_ticket_segment(num, rule, dictionary):
    if num in dictionary.keys():
        dictionary[num].append(rule)
    else:
        dictionary[num] = [rule]


def main():
    rules, tickets = read_input()
    print('Part 1: ' + str(part1(rules, tickets))) #21956
    print('Part 2: ' + str(part2(rules, tickets))) #3709435214239


if __name__ == '__main__':
    main()
