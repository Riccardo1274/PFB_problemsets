#!/usr/bin/env python3
import sys
value = int(sys.argv[1])
if value > 0: #testo se i valori inseriti siano positivi, negativi, sopra o sotto al 50
   print('positive')
   if value <50:
       print('value positive but not enough')
   else:
       print('value pisitive and enough')

elif value < 0:
   print('negative')
else:
   print('0')
