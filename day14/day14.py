def part_one(x):
    cave = parse_input(x)
    return cave.drop_sand()

def part_two(x):
    cave = parse_input(x)
    return cave.drop_sand_two()
    return 0
    return cave.slice_two

def parse_input(x):
    lines = [line.split(' -> ') for line in x.split('\n')]
    structures = [[tuple(map(int, pair.split(','))) for pair in line] for line in lines]
    return Cave(structures)

class Cave:
    def __init__(self, st):
        self.start = (500, 0)
        self.structures = st
        self.max_x = max([pair[0] for line in self.structures for pair in line])
        self.max_y = max([pair[1] for line in self.structures for pair in line])
        self.max_x_two = self.max_x * 2
        self.max_y_two = self.max_y + 2
        self.slice = [[0 for _ in range(self.max_y+1)] for _ in range(self.max_x+1)]
        self.slice_two = [[0 for _ in range(self.max_y_two+1)] for _ in range(self.max_x_two+1)]
        for structure in self.structures:
            xa, ya = structure[0]
            for xb, yb in structure[1:]:
                if xa == xb:
                    for y in range(min(ya,yb), max(ya,yb) + 1):
                        self.slice[xa][y] = 1
                        self.slice_two[xa][y] = 1
                elif ya == yb:
                    for x in range(min(xa,xb), max(xa,xb) + 1):
                        self.slice[x][ya] = 1
                        self.slice_two[x][ya] = 1
                xa,ya = xb,yb
        for j in range(len(self.slice_two)):
            self.slice_two[j][self.max_y_two] = 1
        self.max_y_two = self.max_y + 2
        
    
    def drop_sand(self):
        s = self.slice
        i = 0
        coords = self.start
        while True:
            x,y = coords
            if self.down(x,y):         x,y = x,y+1
            elif self.left_diag(x,y):  x,y = x-1,y+1
            elif self.right_diag(x,y): x,y = x+1,y+1
            else:
                if s[x][y]: break
                s[x][y] = 1
                i += 1
                x,y = self.start
            if self.outside_cave(x,y):
                break
            coords = x,y
        return i
    
    def drop_sand_two(self):
        s = self.slice_two
        i = 0
        coords = self.start
        while self.slice_two[coords[0]][coords[1]] != 1:
            x,y = coords
            if self.down(x,y,s,max_y=self.max_y_two):
                x,y = x,y+1
            elif self.left_diag(x,y,s):
                x,y = x-1,y+1
            elif self.right_diag(x,y,s,max_x=self.max_x_two):
                x,y = x+1,y+1
            else:
                s[x][y] = 1
                i += 1
                x,y = self.start
            coords = x,y
        return i
        
    
    def outside_cave(self,x,y, part=1):
        if part == 1:
            max_y = self.max_y
        if part == 2:
            max_y = self.max_y_two
        return x < 0 or x > self.max_x or y < 0 or y > max_y
    
    def down(self,x,y,s=None,max_y=None):
        if s is None:
            s = self.slice
        if max_y is None:
            max_y = self.max_y
        return y == max_y or s[x][y+1] == 0
    
    def left_diag(self,x,y,s=None):
        if s is None:
            s = self.slice
        if x != 0:
            ld = not bool(s[x-1][y+1])
        else: ld = True
        return ld

    def right_diag(self,x,y,s=None,max_x=None):
        if s is None:
            s = self.slice
        if max_x is None:
            max_x = self.max_x
        if x != max_x:
            rd = not bool(s[x+1][y+1])
        else: rd = False
        return rd

with open('./in.txt') as f:
# with open('./sample.txt') as f:
    one = f.read()
    two = one
    print(part_one(one))
    print(part_two(two))