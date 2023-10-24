#!/usr/bin/env python3
from Bio import SeqIO
import statistics
n_contig = 0
fasta_dict = SeqIO.to_dict(SeqIO.parse('D_melanogaster_genomic.fna', 'fasta'))
nt_count_dict = {}
nt_count_dict_single = {}
total_nt = 0
for key in fasta_dict:
#counting contigs
  print(f'The contig number: {n_contig} has this nucleotide count:\n{nt_count_dict_single}')
  n_contig +=1 
  sequence = fasta_dict[key].seq
  nt_count_dict_single = {}
  for nt in sequence:   
        total_nt += 1  #for the N fraction on total
        if nt in nt_count_dict_single:
           nt_count_dict_single[nt] += 1   #creating a dictionary for each contig to see the single contents of nucleotides
        else:
           nt_count_dict_single[nt] = 1
  for nt in sequence:
        if nt in nt_count_dict:
            nt_count_dict[nt] += 1  #count of nucleotides for all contigs together
        else:
            nt_count_dict[nt] = 1
print(f'The contig number: {n_contig} has this nucleot    ide count:\n{nt_count_dict_single}')
print(f'The total nucleotide count is:\n{nt_count_dict}')     
print(f'The number of contigs is: {n_contig}') 
print("The proportion of N is:", nt_count_dict['N']/total_nt)

