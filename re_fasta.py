#!/usr/bin/env python3
import re
#finding all fasta headers
fasta = open('py07.fasta', 'r')
for line in fasta: 
  if re.search(r'>(.\S+)[\s](.+)',line):
   heads = re.match(r'>(.\S+)[\s](.+)',line)
   print(f'id:{heads.group(1)}\t desc:{heads.group(2)}') 
  

