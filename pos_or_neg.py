#!/usr/bin/env python3
import sys
value = int(sys.argv[1])
if value > 0:
   print('positive')
elif value < 0:
   print('negative')
else:
   print('0')
