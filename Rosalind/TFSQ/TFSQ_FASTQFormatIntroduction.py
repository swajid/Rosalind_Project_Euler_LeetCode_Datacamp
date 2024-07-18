from Bio import SeqIO
out = open('../Rosalind_problems/tfsq.fastq', 'w')
SeqIO.convert("../Rosalind_problems/rosalind_tfsq.txt", "fastq", out, "fasta")
