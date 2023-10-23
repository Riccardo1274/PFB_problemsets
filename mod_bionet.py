#!/usr/bin/env python3
import re

dic = {}
list1 = []
print('enter a restriction enzyme name:\n')
enz=input()
print('enter the sequence to cut:\n')
seq_tocut = input()
txt = open('bionet.txt', 'r')
for line in txt:  #creating the dictionary
  values  = re.search(r'(.+\S)\s+(.+)',line)
  dic[values.group(1)]=values.group(2)
print(dic, '\n')
#if enz in dic:    testing
#  print(enz, dic[enz], "found")

for key in dic:   #looking for a given enzyme 
  if re.search(enz, key): 
     print(f'{enz} is available')
     print(dic[key]) #substituting the sequence
     if dic[key].startswith('^'): #subsistuting if the cut site is at the beginning
        a = re.sub(r'N', r'.', dic[key])
        b = a.replace('^', '')
        c = '('+b+')'
        d = re.sub(c, r'^\1', seq_tocut) 
        print(d)
     else:
        a = re.sub(r'N', r'.', dic[key])
        b = re.sub(r
     
