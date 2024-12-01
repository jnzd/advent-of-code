def part_one(input):
    g = parse_input(input)
    d = dijkstra(g)
    return d

def part_two(input):
    # should be using Floyd-Warshall, but this works (veryyyy slowly)
    g = parse_input(input)
    d_min = 2**32
    nodes_a = [n for n in g.nodes if n.elevation == 'a']
    for i, n in enumerate(nodes_a):
        print(f'{i}/{len(nodes_a)}')
        if n.elevation == 'a':
            d = dijkstra(g, start=n)
            if d is not None:
                d_min = min(d_min, d)
    return d_min

def parse_input(input):
    N = len(input)
    M = len(input[0])
    assert all([len(row) == M for row in input])
    nodes = []
    for i, row in enumerate(input):
        node_row = []
        for j, elevation in enumerate(row):
            if elevation == 'S':
                start = Node(i, j)
                n = start
            elif elevation == 'E':
                end = Node(i, j, elevation='z')
                n = end
            else:
                n = Node(i, j, elevation)
            node_row.append(n)
        nodes.append(node_row)
    for i, row in enumerate(nodes):
        for j, node in enumerate(row):
            assert node.x == i and node.y == j
            neighbors = set()
            if i > 0 and node.compare(nodes[i-1][j]):
                neighbors.add(nodes[i-1][j])
            if j > 0 and node.compare(nodes[i][j-1]):
                neighbors.add(nodes[i][j-1])
            if i < N-1 and node.compare(nodes[i+1][j]):
                neighbors.add(nodes[i+1][j])
            if j < M-1 and node.compare(nodes[i][j+1]):
                neighbors.add(nodes[i][j+1])
            node.neighbors = neighbors
    nodes = [n for row in nodes for n in row]
    for n in nodes:
        # print(f'{n} -> {n.neighbors}')
        assert len(n.neighbors) <= 4
    g = Graph(nodes, start, end)
    return g

class Node:
    def __init__(self, x, y, elevation='a', neighbors=None):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.neighbors = neighbors
        self.distance = None
        self.predecessor = None
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.elevation})'
    
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.elevation})'
    
    def compare(self, other):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        e1 = alphabet.index(self.elevation)
        e2 = alphabet.index(other.elevation)
        return e2 - 1 <= e1
        

class Graph:
    def __init__(self, nodes, start, end):
        self.nodes = nodes
        self.start = start
        self.end = end

def dijkstra(g: Graph, start=None, end=None):
    if start is None: start = g.start
    if end is None: end = g.end
    n = start
    for node in g.nodes:
        node.distance = None
    n.distance = 0
    visited = set()
    while len(visited) < len(g.nodes):
        n = min([n for n in g.nodes if n not in visited], key=lambda x: x.distance if x.distance is not None else 2**32)
        if n.distance is None:
            break
        visited.add(n)
        for m in n.neighbors:
            if m not in visited and (m.distance is None or m.distance > n.distance + 1):
                m.distance = n.distance + 1
                m.predecessor = n
    return end.distance

with open('./in.txt') as f:
# with open('./sample.txt') as f:
    input = f.read().split('\n')
    print(part_one(input))
    print(part_two(input))