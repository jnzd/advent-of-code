def part_one(monkeys):
    monkeys = play_rounds_one(monkeys)
    activity = get_activity(monkeys)
    activity.sort(reverse=True)
    return activity[0] * activity[1]

def part_two(monkeys):
    monkeys = play_rounds_two(monkeys)
    activity = get_activity(monkeys)
    activity.sort(reverse=True)
    return activity[0] * activity[1]

def get_activity(monkeys):
    return [monkey['activity'] for monkey in monkeys]

def get_check_values(monkeys):
    return [monkey['test_value'] for monkey in monkeys]

def play_rounds_one(monkeys, num_rounds=20):
    for _ in range(num_rounds):
        for monkey in monkeys:
            monkey['activity'] += len(monkey['items'])
            while len(monkey['items']) > 0:
                worry_level = monkey['operation'](monkey['items'].pop(0))//3
                if worry_level % monkey["test_value"] == 0:
                    target = monkey['true']
                else:
                    target = monkey['false']
                monkeys[target]['items'].append(worry_level)
    return monkeys

def play_rounds_two(monkeys, num_rounds=10000):
    v = get_check_values(monkeys)
    for _ in range(num_rounds):
        for m_idx in range(len(monkeys)):
            monkey = monkeys[m_idx]
            monkey['activity'] += len(monkey['remainders'])
            while len(monkey['remainders']) > 0:
                operation = monkey['operation']
                remainders = monkey['remainders'].pop(0)
                remainders = [operation(remainders[i]) % v[i] for i in range(len(v))]
                if remainders[m_idx] == 0:
                    target = monkey['true']
                else:
                    target = monkey['false']
                monkeys[target]['remainders'].append(remainders)
    return monkeys

def parse_input(input):
    tmp = [[word.replace(',', '') for word in line.strip().split(' ')] for line in input.splitlines() if line != '']
    monkeys = []
    for i in range(0, len(tmp), 6):
        items = [int(x) for x in tmp[i+1][2:]]
        operation = parse_operation(tmp[i+2][3:])
        test_value = int(tmp[i+3][3])
        true = int(tmp[i+4][5])
        false = int(tmp[i+5][5])
        monkey = {'items': items, 'operation': operation, 'test_value': test_value, 'true': true, 'false': false, 'activity': 0}
        monkeys.append(monkey)
    check_values = get_check_values(monkeys)
    for monkey in monkeys:
        remainders = [[level % value for value in check_values] for level in monkey['items']]
        monkey |= {'remainders': remainders}
    return monkeys

def parse_operation(op):
    if op[1] == '+':
        func = lambda a, b: a + b
    elif op[1] == '*':
        func = lambda a, b: a * b

    if op[0] == 'old' and op[2] == 'old':
        return lambda x: func(x, x)
    elif op[0] == 'old':
        return lambda x: func(x, int(op[2]))
    elif op[2] == 'old':
        return lambda x: func(int(op[0]), x)
    else:
        return lambda _: func(int(op[0]), int(op[2]))


# with open('./sample.txt') as f:
with open('./in.txt') as f:
    input = f.read()
    input_copy = input
    monkeys_one = parse_input(input)
    monkeys_two = parse_input(input_copy)
    print(part_one(monkeys_one))
    print(part_two(monkeys_two))
    