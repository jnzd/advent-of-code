def part_one(input):
    a = [input[i][j] for i in range(len(input)) 
                     for j in range(len(input[i])) 
                        if i==0 or
                            i==len(input)-1 or
                            j==0 or
                            j==len(input[i])-1 or
                            all([input[i][j] > input[k][j] for k in range(i)]) or
                            all([input[i][j] > input[i][k] for k in range(j)]) or
                            all([input[i][j] > input[k][j] for k in range(i+1,len(input))]) or
                            all([input[i][j] > input[i][k] for k in range(j+1,len(input[i]))])]
                                                        
    return len(a)

def part_two(input):
    return 0

# with open('./sample.txt') as f:
with open('./in.txt') as f:
    input = [list(x) for x in f.read().split('\n')]
    print(part_one(input))
    print(part_two(input))