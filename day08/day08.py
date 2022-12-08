def part_one(x):
    assert all(len(x) == len(x) for x in x)
    n = len(x)
    a = [x[i][j] for i in range(n) 
                 for j in range(n) 
                    if i==0 or
                       i==len(x)-1 or
                       j==0 or
                       j==len(x[i])-1 or
                       all([x[i][j] > x[k][j] for k in range(i)]) or
                       all([x[i][j] > x[i][k] for k in range(j)]) or
                       all([x[i][j] > x[k][j] for k in range(i+1,n)]) or
                       all([x[i][j] > x[i][k] for k in range(j+1,n)])]
    return len(a)

def part_two(x):
    assert all(len(x) == len(x) for x in x)
    n = len(x)
    a = [[len([x[i][k] for k in range(j) if all(x[i][l] < x[i][j] for l in range(k,j))]) if j > 0 else 0 for j in range(n)] for i in range(n)]
    a = [[a[i][j] + 1 if a[i][j] < j else a[i][j] for j in range(n)] for i in range(n)]
    b = [[len([x[i][k] for k in range(j+1,n) if all(x[i][l] < x[i][j] for l in range(j+1,k))]) if j < n-1 else 0 for j in range(n)] for i in range(n)]
    c = [[len([x[k][j] for k in range(i) if all(x[l][j] < x[i][j] for l in range(k,i))]) if i > 0 else 0 for j in range(n)] for i in range(n)]
    c = [[c[i][j] + 1 if c[i][j] < i else c[i][j] for j in range(n)] for i in range(n)]
    d = [[len([x[k][j] for k in range(i+1,n) if all(x[l][j] < x[i][j] for l in range(i+1,k))]) if i < n-1 else 0 for j in range(n)] for i in range(n)]
    a = [a[i][j] for i in range(n) for j in range(n)]
    b = [b[i][j] for i in range(n) for j in range(n)]
    c = [c[i][j] for i in range(n) for j in range(n)]
    d = [d[i][j] for i in range(n) for j in range(n)]
    return max([a[i]*b[i]*c[i]*d[i] for i in range(n*n)])

# with open('./sample.txt') as f:
with open('./in.txt') as f:
    input = [[int(y) for y in list(x)] for x in f.read().split('\n')]
    print(part_one(input))
    print(part_two(input))