#!/usr/bin/env python3
from Bio import SeqIO
import re
import statistics
length_max = 0
total_length = 0
length_min = 100000000000000000000000000000000000000000
fasta_dict = SeqIO.to_dict(SeqIO.parse('ecoli025.txt', 'fasta'))  #creating a dictionary for the fasta
list_length =[] 
for key in fasta_dict.keys(): 
  sequence = fasta_dict[key].seq #extracting the sequence from the dictionary
  length = len(sequence)
  total_length += length
  list_length.append(length)
  if length >= length_max: 
    length_max = length #finding the maximum length
  elif length <= length_min:      
    length_min = length #finding the minimum length
  else:
   continue
nt50 = statistics.median(list_length) #calculating the NT50
lt50 = 0
for key in fasta_dict.keys():
   sequence = fasta_dict[key].seq
   if len(sequence) >= nt50:
     lt50 += 1 #calculating the LT50


print(f'This is the max length: {length_max}')
print(f'This is the min length: {length_min}')
print(f'This is the total length: {total_length}')
print(f'This is the NT50: {nt50}')
print(f'This is the LT50: {lt50}')

