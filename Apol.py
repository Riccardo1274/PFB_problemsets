#!/usr/bin/env python3
import re
#finding the sites for restriction enzyme Apol
fasta = open('apol.fasta', 'r')
final_string=''
for line1 in fasta:
   sub = re.sub(r'([AG]AATT[CT])', r'\1^',line1)
   final_string += sub
final_string=final_string.replace('\n', '')
print(final_string)

sep=final_string.split('^')
dic = {}
for line in sep:
  dic[len(line)] = line
for seq in sorted(dic):
  print(seq , '-->', dic[seq])

