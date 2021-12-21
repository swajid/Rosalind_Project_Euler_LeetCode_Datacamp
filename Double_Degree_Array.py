# Double-Degree Array
# https://rosalind.info/problems/ddeg/

import pandas as pd
from igraph import *

df = pd.read_csv("ddegarray.txt", sep='\s+')
g = Graph(df.apply(tuple, axis=1).tolist())

for x in range(1,1001):
    if (x in df.iloc[:, 0].tolist() or x in df.iloc[:, 1].tolist()):
        print(sum(g.degree(g.neighbors(x))), end =" ")
    else:
        print(0, end =" ")
