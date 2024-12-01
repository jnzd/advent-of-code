def solve(input, l):
    return [i for i in range(l-1, len(input)) if len(set(input[i-l:i])) == l][0]
    
# with open('./sample1.txt') as f:
# with open('./sample2.txt') as f:
# with open('./sample3.txt') as f:
# with open('./sample4.txt') as f:
# with open('./sample5.txt') as f:
with open('./in.txt') as f:
    input = f.read()
    print(solve(input, 4))
    print(solve(input, 14))