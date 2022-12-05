import re

def part_one(stacks, moves):
    for count, stack_from, stack_to in moves:
        for _ in range(count):
            stacks[stack_to-1].append(stacks[stack_from-1].pop())
    return ''.join([stack[-1] for stack in stacks])

def part_two(stacks, moves):
    for count, stack_from, stack_to in moves:
        stacks[stack_to-1] = stacks[stack_to-1] + stacks[stack_from-1][-count:]
        stacks[stack_from-1] = stacks[stack_from-1][:-count]
    return ''.join([stack[-1] for stack in stacks])

def make_stacks(stack_matrix):
    stacks = list(map(list, zip(*stack_matrix)))
    stacks = [list(reversed(stack[:-1])) for stack in stacks if all([xi in '1234567890' for xi in stack[-1]])]
    stacks = [[i for i in stack if i != ' '] for stack in stacks]
    return stacks
    
with open('in.txt') as f:
# with open('sample.txt') as f:
    stack_drawing, moves = f.read().split('\n\n')
    stack_matrix = [list(line) for line in stack_drawing.split('\n')]
    pattern = r'move (\d*) from (\d*) to (\d*)'
    moves = [list(map(int, m.groups())) for line in moves.split('\n') for m in re.finditer(pattern, line)]
    stacks = make_stacks(stack_matrix)
    print(part_one(stacks, moves))
    stacks = make_stacks(stack_matrix)
    print(part_two(stacks, moves))