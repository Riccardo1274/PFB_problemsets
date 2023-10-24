#!/usr/bin/env python3
from Bio import SeqIO
import statistics
n_contig = 0
fasta_dict = SeqIO.to_dict(SeqIO.parse('D_melanogaster_genomic.fna', 'fasta'))
for key in fasta_dict:
  n_contig +=1
  sequence = fasta_dict[key].seq
print(n_contig) 
 
