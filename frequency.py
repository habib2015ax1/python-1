frequency ={"habib":1,"carter":3,"omar":6,"ali":9,"jad":6}
count=0
Search=6
for key,value in frequency.items():
    if Search==frequency.get(key):
     count=count+1
print (count)