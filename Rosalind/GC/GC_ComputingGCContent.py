import numpy as np

def gc_content(sequence):
    out = (((sequence.count('G')+sequence.count('C'))/len(sequence)))*100
    return np.round(out,6)
    
max_seq_id = ""
max_gc = 0
from Bio import SeqIO
for seq_record in SeqIO.parse("../Rosalind_problems/rosalind_gc.fasta.txt", "fasta"):
#    print(seq_record.id)
#    print(repr(seq_record.seq))
#    print(len(seq_record))
#    print(seq_gc_content)
    seq_gc_content = gc_content(seq_record.seq)
    if seq_gc_content > max_gc:
        max_seq_id = seq_record.id
        max_gc = seq_gc_content

print(max_seq_id)
print(max_gc)