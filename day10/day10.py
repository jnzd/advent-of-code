def part_one(input):
    trace = calc_trace(input)
    return sum([i * trace[i] for i in range(20, len(trace), 40)])

def calc_trace(input):
    x = 1
    trace = [x]
    input = [[a[0], int(a[1])] if len(a) == 2 else a[0] for a in [line.split(' ') for line in input]]
    for cmd in input:
        trace.append(x)
        if cmd[0] == 'addx':
            trace.append(x)
            x += cmd[1]
    return trace

def part_two(input):
    trace = calc_trace(input)
    crt = [['|' for _ in range(42)] for _ in range(8)]
    for i in range(1,7):
        for j in range(1,41):
            k = (i-1)*40 + j
            if (j-1) in range(trace[k]-1, trace[k]+2):
                # crt[i][j] = '#'
                crt[i][j] = '█'
            else:
                # crt[i][j] = '.'
                crt[i][j] = ' '
    for i in range(len(crt)):
        print(''.join(crt[i]))
    return crt

# with open('./sample-small.txt') as f:
# with open('./sample.txt') as f:
with open('./in.txt') as f:
    input = f.read().splitlines()
    print(part_one(input))
    part_two(input)