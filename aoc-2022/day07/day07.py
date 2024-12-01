def part_one(input, size_limit=100000):
    filesystem = get_filesystem(input)    
    sizes = get_sizes(filesystem)
    return sum([i['size'] for _, i in sizes.items() if i['size'] < size_limit and i['is_dir']])

def get_filesystem(input):
    lines = input.splitlines()
    filesystem = dict()
    cur_dir = filesystem
    for line in lines:
        words = line.split(' ')
        if words[0] == '$' and words[1] == 'cd':
            if words[2] == '..': 
                cur_dir = cur_dir['parent']
            else:
                path = make_path(cur_dir, words[2])
                if path not in cur_dir.keys():
                    cur_dir |= {path: {'parent': cur_dir, 'path': path}}
                cur_dir = cur_dir[path]
        elif words[0] != '$' and words[0] != 'dir':
            path = make_path(cur_dir, words[1])
            cur_dir |= {path: int(words[0])}
    return filesystem

def make_path(cur_dir, key):
    if cur_dir is None or len(cur_dir) == 0:
        return key
    return cur_dir['path'] + key + '/'

def get_sizes(tree):
    result = dict()
    for key in tree.keys():
        if key == 'parent' or key == 'path':
            continue
        elif type(tree[key]) == dict:
            sub_result = get_sizes(tree[key])
            dir_size = sum([i['size'] for k, i in sub_result.items() if k in tree[key].keys()])
            result |= {key: {'size': dir_size, 'is_dir': True}} | sub_result
        else:
            result |= {key: {'size': tree[key], 'is_dir': False}}
    return result

def part_two(input, total_disk_space=70000000, needed_space=30000000):
    file_system = get_filesystem(input)
    sizes = get_sizes(file_system)
    free_space = total_disk_space - sizes['/']['size']
    if free_space >= needed_space:
        return 0
    return min([i['size'] for _, i in sizes.items() if i['is_dir'] and i['size'] > needed_space - free_space])

# with open('sample.txt') as f:
with open('in.txt') as f:
    input = f.read()
    print(part_one(input))
    print(part_two(input))