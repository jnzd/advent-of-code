with open('./in.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

# The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

# To do this, count the number of times a depth measurement increases from the previous measurement.

c = -1 
pre = 0

for curr in lines:
    if int(curr) > pre:
        c += 1
    pre = int(curr)


print(c)
