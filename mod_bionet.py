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

for key in dic.keys():   #looking for a given enzyme 
   print(re.findall(enz, key)) 
#  if re.search(r'enz', key) is True:  
 #   print(f'{enz} is available: is site is {dic[key]}')


