#!/usr/bin/env python3
import sys
beginning_fasta =open(sys.argv[1], 'r')
t_list=[]
dictionary={} #creating a dictionary with the fasta
for line in beginning_fasta:
  t_list=line.split('\t')
  dictionary[t_list[0]]=t_list[1]
print (dictionary)
  

