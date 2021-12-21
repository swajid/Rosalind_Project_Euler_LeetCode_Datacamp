# https://rosalind.info/problems/deg/

import pandas as pd
from igraph import *

df = pd.read_csv("degarray.txt", sep='\s+')
g = Graph(df.apply(tuple, axis=1).tolist())
print(*g.degree()[1:], sep=' ')
