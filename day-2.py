lines = open('day-2.txt').read().split('\n')
pairs = [l.split(' ') for l in lines]

# Puzzle 1
forward = [int(b) for a,b in pairs if 'forward' in a]
down = [int(b) for a,b in pairs if 'down' in a]
up = [int(b) for a,b in pairs if 'up' in a]

print('Puzzle 1:', (sum(down)-sum(up))*sum(forward))

# Puzzle 2
aim, depth, horizontal = 0, 0, 0

for a,b in pairs:
    num = int(b)
    dir = a[:1]
    if dir == 'f':
        horizontal += num
        depth += aim*num
    if dir == 'u':
        aim -= num
    if dir == 'd':
        aim += num

print('Puzzle 2:', depth*horizontal)