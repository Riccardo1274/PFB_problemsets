#!/usr/bin/env python3
import re
#finding the sites for restriction enzyme Apol
fasta = open('apol.fasta', 'r')
for line1 in fasta:
   sub = re.sub(r'([AG]AATT[CT])', r'\1^',line1)
   print(sub)
