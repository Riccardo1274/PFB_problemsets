#!/usr/bin/env python3
fastq = open('fastq.fastq', 'r')
length=0
count=0
for line in fastq:
 count+=1
 length = length + len(line)
print(f'the number of lines is {count}')
print(f'the number of characters is {length}')
print('the average line length is', length/count)
