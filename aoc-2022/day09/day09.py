def part_one(input):
    head = (0,0)
    tail = (0,0)
    visited = {tail}
    for line in input:
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            head, tail = move(head, tail, direction)
            visited.add(tail)
    return len(visited)

def move(head, tail, direction):
    xh, yh = head
    if direction == 'U':   yh += 1
    elif direction == 'D': yh -= 1
    elif direction == 'R': xh += 1
    elif direction == 'L': xh -= 1
    head = (xh, yh)
    if not touching(head, tail):
        tail = adjust(head, tail)
    return head, tail

def touching(head, tail):
    x1, y1 = head
    x2, y2 = tail
    return ((x1 == x2 and abs(y1 - y2) == 1) or 
            (y1 == y2 and abs(x1 - x2) == 1) or 
            (x1 == x2 and y1 == y2) or 
            (abs(x1 - x2) == 1 and abs(y1 - y2) == 1))

def adjust(head, tail):
    xh, yh = head
    xt, yt = tail
    dx = xh - xt
    dy = yh - yt
    if dx == 0:
        if   dy == 2:  yt += 1
        elif dy == -2: yt -= 1
    elif dy == 0:
        if   dx == 2:  xt += 1
        elif dx == -2: xt -= 1
    else:
        if   dx > 0: xt += 1
        elif dx < 0: xt -= 1
        if   dy > 0: yt += 1
        elif dy < 0: yt -= 1
    return (xt, yt)

def part_two(input):
    knots = [(0,0) for _ in range(10)]
    visited = {knots[-1]}
    for line in input:
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            knots = move_two(knots, direction)
            visited.add(knots[-1])
    return len(visited)

def move_two(knots, direction):
    xh, yh = knots[0]
    if direction == 'U':
        yh += 1
    elif direction == 'D':
        yh -= 1
    elif direction == 'R':
        xh += 1
    elif direction == 'L':
        xh -= 1
    knots[0] = (xh, yh)
    for i in range(1, len(knots)):
        if not touching(knots[i-1], knots[i]):
            knots[i] = adjust(knots[i-1], knots[i])
    return knots

# with open('./sample.txt') as f:
# with open('./sample2.txt') as f:
with open('./in.txt') as f:
    input = f.read().splitlines()
    print(part_one(input))
    print(part_two(input))


