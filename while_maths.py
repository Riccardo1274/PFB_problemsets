#!/usr/bin/env python3
#creating a script to print all numbers from 1 to 100
count=0
while count < 100:
  count += 1
  print(count)
print('finish')
#counting 1000!
count1000=0
fact=1
while count1000 < 1000:
 count1000 += 1
 fact = fact*count1000
print(fact)
#printing even from a known list
values = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
for num in values:
  even=num%2
  if even==0:
    print(num)
#summing the evens with evens and odds with odds
print(values)
sum_even=0
sum_odds=0
for num in values:
  print(num)
  even2=num%2
  if even2==0:
    sum_even += num
  else:
    sum_odds += num
print(sum_even)
print(sum_odds)
    
