import itertools
n = 3
s="A B C D E F"
kmer = list(map(str,s.split()))
x = list(itertools.product(kmer, repeat=n))
for item in list(x):
  print(''.join(item))