#!/usr/bin/env python3
import re
#looking for all the nobody in nobody
txt_out = open('ioio.txt', 'w')
line_count=0
nobody = open('nobody.txt', 'r') 
for line in nobody:
 found_nobody = re.findall(r'Nobody',line)
 line_count+=1
 print('in the line', line_count, 'we found', len(found_nobody))
 x=line.replace('Nobody', 'ioio')
 txt_out.write(x + '\n')
