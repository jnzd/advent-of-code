def is_dec(l):
    for i in range(len(l)-1):
        if l[i] <= l[i+1] or l[i] - l[i+1] > 3:
            return False
    return True

def is_inc(l):
    for i in range(len(l)-1):
        if l[i] >= l[i+1] or l[i+1] - l[i] > 3:
            return False
    return True

def is_safe(l):
    # print(f"{l} {is_dec(l)} {is_inc(l)}")
    return is_dec(l) or is_inc(l)

def is_dec_2(l):
    for i in range(len(l)):
        if i == 0 and is_dec(l[1:]):
            return True
        elif i == len(l)-1 and is_dec(l[:-1]):
            return True
        elif is_dec(l[:i] + l[i+1:]) and is_dec([l[i-1]] + l[i+1:]):
            return True
    return False

def is_inc_2(l):
    for i in range(len(l)):
        if i == 0 and is_inc(l[1:]):
            return True
        elif i == len(l)-1 and is_inc(l[:-1]):
            return True
        elif is_inc(l[:i] + l[i+1:]) and is_inc([l[i-1]] + l[i+1:]):
            return True
    return False

def is_safe_2(l):
    # print(f"{l} {is_dec(l)} {is_inc(l)}")
    return is_dec_2(l) or is_inc_2(l)

# with open('sample.txt') as f:
with open('input.txt') as f:
    lines = f.readlines()
    nums = [[int(x) for x in line.split()] for line in lines]
    print("Part 1")
    safe_nums = [num for num in nums if is_safe(num)]
    print(len(safe_nums))

    print("Part 2")
    safe_nums_2 = [num for num in nums if is_safe_2(num)]
    print(len(safe_nums_2))
