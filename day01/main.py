def solve(input_path):
    with open(input_path) as f:
        data = [d.splitlines() for d in f.read().split('\n\n')]
        data = [[int(d) for d in dd] for dd in data]
        data = [sum(d) for d in data]
        return max(data)


print(solve('./sample.txt'))
print(solve('./in.txt'))