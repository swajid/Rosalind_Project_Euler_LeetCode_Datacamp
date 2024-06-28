from Bio import Entrez
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term='Olmeca [Organism] AND (2007/10/03[Publication Date] : 2012/12/14[Publication Date])')
record = Entrez.read(handle)
record["Count"]
