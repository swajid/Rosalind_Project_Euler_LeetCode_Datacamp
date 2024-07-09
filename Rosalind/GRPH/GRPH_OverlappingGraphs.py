import itertools

fasta_dict = {}
from Bio import SeqIO
for seq_record in SeqIO.parse("../Rosalind_problems/rosalind_grph.fasta.txt", "fasta"):
#    print(seq_record.id)
#    print(seq_record.seq)
    fasta_dict[seq_record.id] = str(seq_record.seq)

#for key,value in fasta_dict:
	#print(fasta_dict.keys())
	#print(fasta_dict.values())
	#print(fasta_dict)

# beginning and end, 3
def is_3_overlap(seq1, seq2):
    return seq1[-3:] == seq2[:3]

# https://docs.python.org/3/library/itertools.html#itertools.combinations
def make_edges(fasta_dict):
    edges = []
    for A, B in itertools.combinations(fasta_dict, 2):
        seq_A, seq_B = fasta_dict[A], fasta_dict[B]

        if is_3_overlap(seq_A, seq_B):
            edges.append((A,B))

        if is_3_overlap(seq_B, seq_A):
            edges.append((B,A))

    return edges

out = make_edges(fasta_dict)

for key, value in out:
    print("{} {}".format(key, value))