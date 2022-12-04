def part_one(input):
    segments = get_segments(input)
    fully_contained = [seg for seg in segments if seg[0][0] <= seg[1][0] and 
                                                  seg[0][1] >= seg[1][1] or 
                                                  seg[0][0] >= seg[1][0] and 
                                                  seg[0][1] <= seg[1][1]]
    return len(fully_contained)

def part_two(input):
    segments = get_segments(input)
    overlap = [seg for seg in segments if seg[0][0] in range(seg[1][0], seg[1][1] + 1) or 
                                          seg[0][1] in range(seg[1][0], seg[1][1] + 1) or 
                                          seg[1][0] in range(seg[0][0], seg[0][1] + 1) or 
                                          seg[1][1] in range(seg[0][0], seg[0][1] + 1)]
    return len(overlap)

def get_segments(input):
    segments = [tuple(tuple(int(x) for x in seg_range.split('-')) for seg_range in line.split(',')) for line in input.split('\n')]
    return segments

# with open('sample.txt') as f:
with open('in.txt') as f:
    input = f.read()
    print(part_one(input))
    print(part_two(input))