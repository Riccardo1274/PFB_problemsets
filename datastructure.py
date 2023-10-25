#!/usr/bin/env python3
import sys

#counting acgt content in a fasta with a fata structure to store the information
head = 'to_sub'
seq_tot = ''
beginning_fasta =open(sys.argv[1], 'r')
t_list=['to_sub', 'to_sub']
fasta_dict = {} #creating a dictionary with the fasta
for line in beginning_fasta:
  if line.startswith('>'):  #if i have the header, i just add it but when the for loop finished te seq
     seq_tot = ''.join(t_list) #faster way to compact a string
     fasta_dict[head] = seq_tot 
     seq_tot = ''  
     head = line.replace('\n', '')
     t_list = []
  else:
     seq = line.replace('\n', '')
     t_list.append(seq) # creating the list to compact the sequence
seq_tot = ''.join(t_list)
fasta_dict[head] = seq_tot #adding the last sequence
#creating a dictionary in the fasta dict with the numbers of nucleotides
nt_dict ={}
for key in fasta_dict:
  nA = fasta_dict[key].count('A')
  nC = fasta_dict[key].count('C')
  nG = fasta_dict[key].count('G')
  nT = fasta_dict[key].count('T')
  
  nt_dict[key] = {fasta_dict[key] : {'A' : nA, 'C' : nC, 'G' : nG, 'T' : nT}}
print(nt_dict)

