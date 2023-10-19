#!/usr/bin/env python3
import sys
beginning_fasta =open(sys.argv[1], 'r')
fasta = open(sys.argv[2], 'w')
dictionary={}
#printing the reverse complement
for line in beginning_fasta:
 t_list = line.split('\t')
 #printing the reverse complement
 a=t_list[1].replace('A', 'a')
 c=a.replace('C', 'c')
 g=c.replace('G', 'g')
 t=g.replace('T', 't') #creating a subsequence to substitute
 T=t.replace('a', 'T')
 G=T.replace('c', 'G')
 C=G.replace('g', 'C')
 dna_complement=C.replace('t', 'A') #created the complement
 dna_rev_com=dna_complement[::-1]
 fasta.write(f'{t_list[0]}\t{dna_rev_com}\n')
print(f'Wrote the reverse complement in {sys.argv[2]}') 

