import ast
def part_one(x):
    res = [i+1 for i,c in enumerate([compare(y) for y in x]) if c]
    return sum(res)

def part_two(x):
    divider_packets = [[[2]],[[6]]]
    x += divider_packets
    y = sort(x)
    return (y.index([[2]])+1) * (y.index([[6]])+1)

def parse_one(input):
    pairs = [[ast.literal_eval(y) for y in x.split('\n')] for x in input.split('\n\n')]
    return pairs

def parse_two(input):
    packets = [ast.literal_eval(x) for x in input.split('\n') if x != '']
    return packets

def compare_element(a, b):
    if a<b:   return True
    elif a>b: return False
    else:     return None

def compare(x):
    assert len(x) == 2
    a = x[0].copy()
    b = x[1].copy()
    if len(a) == 0 and len(b) != 0:   return True
    elif len(a) != 0 and len(b) == 0: return False
    elif len(a) == 0 and len(b) == 0: return None
    if type(a[0]) == int and type(b[0]) == int:
        res = compare_element(a[0], b[0])
    else:
        if type(a[0]) != list: a[0] = [a[0]]
        if type(b[0]) != list: b[0] = [b[0]]
        res = compare([a[0], b[0]])
    if res is not None: return res
    return compare([a[1:], b[1:]])

def sort(x):
    while not is_sorted(x):
        for i in range(0, len(x)-1):
            if not compare([x[i], x[i+1]]):
                x[i], x[i+1] = x[i+1], x[i]
    return x
        
def is_sorted(x):
    return all([compare([x[i], x[i+1]]) for i in range(len(x)-1)])

with open('./in.txt') as f:
# with open('./sample.txt') as f:
    one = f.read()
    two = one
    in_one = parse_one(one)
    in_two = parse_two(two)
    print(part_one(in_one))
    print(part_two(in_two))