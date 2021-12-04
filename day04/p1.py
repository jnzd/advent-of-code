with open("in.txt", "r") as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))
    winningNumbers = lines[0]
    
    
    # words = list(map(lambda x: x.split(), lines))
    print(lines)
    # print(words)