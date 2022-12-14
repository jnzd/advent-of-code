def part_one(x):
    cave = parse_input(x)
    return cave.drop_sand()

def part_two(x):
    return x

def parse_input(x):
    lines = [line.split(' -> ') for line in x.split('\n')]
    structures = [[tuple(map(int, pair.split(','))) for pair in line] for line in lines]
    return Cave(structures)

class Cave:
    def __init__(self, st):
        # shift everything to the left
        self.offset = min([pair[0] for line in st for pair in line])
        self.start = (500-self.offset, 0)
        self.structures = [[(pair[0]-self.offset, pair[1]) for pair in line] for line in st]
        self.max_x = max([pair[0] for line in self.structures for pair in line])
        self.max_y = max([pair[1] for line in self.structures for pair in line])
        self.slice = [[0 for _ in range(self.max_y+1)] for _ in range(self.max_x+1)]
        for structure in self.structures:
            xa, ya = structure[0]
            for xb, yb in structure[1:]:
                if xa == xb:
                    for y in range(min(ya,yb), max(ya,yb) + 1):
                        self.slice[xa][y] = 1
                elif ya == yb:
                    for x in range(min(xa,xb), max(xa,xb) + 1):
                        self.slice[x][ya] = 1
                xa,ya = xb,yb
    
    def drop_sand(self):
        i = 0
        coords = self.start
        # print(f'sand {i+1}')
        while True:
            x,y = coords
            if self.down(x,y):
                x,y = x,y+1
                # print(f'   {i+1} moved down {(x,y-1)} -> {(x,y)}')
            elif self.left_diag(x,y):
                x,y = x-1,y+1
                # print(f'   {i+1} moved left diag {(x+1,y-1)} -> {(x,y)}')
            elif self.right_diag(x,y):
                x,y = x+1,y+1
                # print(f'   {i+1} moved right diag {(x-1,y-1)} -> {(x,y)}')
            else:
                # print(f'   {i+1} stuck at {(x,y)}')
                if self.slice[x][y]:
                    break
                self.slice[x][y] = 1
                i += 1
                x,y = self.start
                # print(f'sand {i+1}')
            if self.outside_cave(x,y):
                # print(f'   {i+1} fell out of cave at {(x,y)}')
                break
            coords = x,y
        return i
    
    def outside_cave(self,x,y):
        return x < 0 or x > self.max_x or y < 0 or y > self.max_y
    
    def down(self,x,y):
        return y == self.max_y or self.slice[x][y+1] == 0
    
    def left_diag(self,x,y):
        if x != 0:
            ld = not bool(self.slice[x-1][y+1])
        else: ld = True
        return ld

    def right_diag(self,x,y):
        if x != self.max_x:
            rd = not bool(self.slice[x+1][y+1])
        else: rd = False
        return rd

with open('./in.txt') as f:
# with open('./sample.txt') as f:
    one = f.read()
    two = one
    print(part_one(one))
    print(part_two(two))