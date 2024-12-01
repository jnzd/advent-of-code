def solve_part1(input_path):
    with open(input_path) as f:
        data = [d.splitlines() for d in f.read().split('\n\n')]
        data = [[int(d) for d in dd] for dd in data]
        data = [sum(d) for d in data]
        return max(data)


def solve_part2(input_path):
    with open(input_path) as f:
        data = [d.splitlines() for d in f.read().split('\n\n')]
        data = [[int(d) for d in dd] for dd in data]
        data = [sum(d) for d in data]
        res = 0
        for _ in range(3):
            top = max(data)
            data.remove(top)
            res += top
        return res


print(solve_part1('./sample.txt'))
print(solve_part2('./sample.txt'))
print(solve_part1('./in.txt'))
print(solve_part2('./in.txt'))