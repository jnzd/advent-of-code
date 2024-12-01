with open('input.txt', encoding='utf-8') as f:
# with open('sample.txt', encoding='utf-8') as f:
    # Part 1
    print("Part 1")
    data = f.read().splitlines()
    nums = [x.split() for x in data]
    nums = [(int(i), int(j)) for [i,j] in nums]
    c0 = [x[0] for x in nums]
    c1 = [x[1] for x in nums]
    c0_sorted = sorted(c0)
    c1_sorted = sorted(c1)
    c_sorted = zip(c0_sorted, c1_sorted)
    diffs = [abs(x[0] - x[1]) for x in c_sorted]
    print(sum(diffs))

    # Part 2
    print("Part 2")
    values = [x * c1.count(x) for x in c0]
    print(sum(values))

