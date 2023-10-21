#!/usr/bin/env python3
import re
dic = {}
list1 = []
txt = open('bionet.txt', 'r')
for line in txt:
  values  = re.search(r'(.+\S)\s+(.+)',line)
  dic[values.group(1)]=values.group(2)
print(dic)
