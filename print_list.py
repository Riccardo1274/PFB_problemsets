#!/usr/bin/env python3
#print with for each element of a list
seqs=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in seqs:
  
  print(len(seq),'\t',seq,'\t',seqs.index(seq))
#creating a list of tuplets with seq and len
dupl=[]
for seq in seqs:
  length=len(seq)
  dupl.append((length,seq))
print(dupl)
  
