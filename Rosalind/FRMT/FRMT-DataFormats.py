from Bio import Entrez, SeqIO
email_id = "sanawgs@gmail.com"

def all_entries(ids):
    Entrez.email = email_id
    handle = Entrez.efetch(db="nucleotide", id=[", ".join(ids)], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    print(min(records, key=lambda s: len(s.seq)).format("fasta"))

s = "JX295575 JN573266 BT149870 JX462669 FJ817486 NM_001015511 NM_001194889 JX469991 JQ712982 JQ342169"
ids = list(map(str,s.split()))
all_entries(ids)