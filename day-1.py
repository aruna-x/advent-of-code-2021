# f = open('day-1.txt')
# text = f.read()
# lines = text.split('\n')
# nums = [int(l) for l in lines]
# pairs = zip(nums[:-1], nums[1:])
# bigs = [1 for a,b in pairs if b > a]
# res = sum(bigs)
# print(res)

def find_bigs(pairs):
    return [1 for a,b in pairs if b > a]

lines = open('day-1.txt').read().split('\n')
nums = [int(l) for l in lines]

# Puzzle 1
bigs_1 = find_bigs(zip(nums[:-1], nums[1:]))
print("Puzzle 1:", sum(bigs_1))

# Puzzle 2
window_sums = [sum(nums[i:i+3]) for i in range(len(nums[:-2]))]
bigs_2 = find_bigs(zip(window_sums[:-1], window_sums[1:]))
print("Puzzle 2:", sum(bigs_2))