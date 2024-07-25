import itertools
k = 3
s = 'ZLKPAEWXIS'
perm = []
for i in range(1, k + 1):
    perm.append([''.join(p) for p in itertools.product(s, repeat=i)])
permutations = list(itertools.chain(*perm))

def sort_key(word):
    return [s.index(c) for c in word]
perm_s = sorted(permutations, key=sort_key)

print(*perm_s, sep = "\n")