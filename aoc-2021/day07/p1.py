with open("in.txt") as f:
# with open("in-sample.txt") as f:
    positions = list(map(int, f.read().split(",")))
    maxPos = max(positions)
    p1cost = sum(positions)
    p2cost = maxPos * sum(positions)
    for i in range(maxPos):
        p1costTmp = sum(map(lambda x: abs(x-i), positions))
        p1cost = min(p1cost, p1costTmp)
        p2costTmp = sum(map(lambda x: int(abs(x-i) * (abs(x-i)+1) / 2), positions))
        p2cost = min(p2cost, p2costTmp)

    print(p1cost)
    print(int(p2cost))

