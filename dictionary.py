#!/usr/bin/env python3
#creating a dictionary
fav={'animal' : 'Freddy' , 'bird' : 'Motacilla flava' , 'activity' : 'ringing'}
print(fav)
print(fav['bird'])
fav['bird']=input("Which is your favourite bird?")
fav_t='activity'
print(fav[fav_t])
fav['name']='lupoalberto'
print(fav)
fav['name']='lupolucio'
for favs in fav:
  print(favs,'\t', fav[favs])
