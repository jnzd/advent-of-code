import re

def part_one(input):
    covered_points = set()
    beacons = {(xb, yb) for _, _, xb, yb in input}
    for i, (xs, ys, xb, yb) in enumerate(input):
        print(f'sensor {i+1} of {len(input)}')
        d = abs(xs-xb) + abs(ys-yb)
        # y = 10
        y = 2000000
        for x in range(xs-d, xs+d+1):
            if abs(x-xs) + abs(y-ys) <= d and (x, y) not in beacons:
                covered_points.add((x, y))
    return len(covered_points)

def inside_bound(x,bound):
    return x >= 0 and x <= bound

def part_two(input):
    # bound = 20+1
    bound = 4000000+1
    points_directly_outside = set()
    for i, (xs, ys, xb, yb) in enumerate(input):
        print(f'diamond {i+1} of {len(input)}')
        d = abs(xs-xb) + abs(ys-yb) + 1
        for a in range(d):
            x1 = xs - a
            y1 = ys - d + a
            x2 = xs + a
            y2 = ys + d - a
            x1_inside = inside_bound(x1, bound)
            y1_inside = inside_bound(y1, bound)
            x2_inside = inside_bound(x2, bound)
            y2_inside = inside_bound(y2, bound)
            if x1_inside and y1_inside:
                points_directly_outside.add((x1, y1))
            if x2_inside and y2_inside:
                points_directly_outside.add((x2, y2))
            if x1_inside and y2_inside:
                points_directly_outside.add((x1, y2))
            if x2_inside and y1_inside:
                points_directly_outside.add((x2, y1))
            assert abs(x1-xs) + abs(y1-ys) == d
            assert abs(x2-xs) + abs(y2-ys) == d
            assert abs(x1-xs) + abs(y2-ys) == d
            assert abs(x2-xs) + abs(y1-ys) == d
    
    for i, (x,y) in enumerate(points_directly_outside):
        outside = True
        for i, (xs, ys, xb, yb) in enumerate(input):
            if abs(x-xs) + abs(y-ys) <= abs(xs-xb) + abs(ys-yb):
                outside = False
                break
        if outside:
            return x*4000000 + y
            
def parse(x):
    r = r'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)'
    return [list(map(int, m.groups())) for line in x.split('\n') for m in re.finditer(r, line)]

with open('./in.txt') as f:
# with open('./sample.txt') as f:
    in_one = f.read()
    in_two = in_one
    x_one = parse(in_one)
    x_two = parse(in_two)
    print(part_one(x_one))
    print(part_two(x_two))
