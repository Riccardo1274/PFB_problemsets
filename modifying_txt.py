#!/usr/bin/env python3
import sys
txt_obj = open(sys.argv[1])
num_line = 0
pyot = open(sys.argv[2], 'w')
for line in txt_obj:
  num_line += 1
  print(num_line, line)
  pyot.write(line)
print(pyot)


