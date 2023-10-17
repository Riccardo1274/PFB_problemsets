#!/usr/bin/env python3
import sys
value = int(sys.argv[1])
if value > 0: #testo se i valori inseriti siano positivi, negativi, sopra o sotto al 50
   print('positive')
   if value <50:
       print('value positive but not enough')
       if value%2 == 0:
          print('value is also even')
       else:
          print('value is not even')
   else:
       print('value positive and enough')
       if value%3 == 0:
             print('divisble by 3')
       else:
             print('not divisible by 3')

elif value < 0:
   print('negative')
else:
   print('0')
