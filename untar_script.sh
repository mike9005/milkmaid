#!/bin/bash

extract="-jxf"
FILES="/Volumes/MilkMaid/raw_source/*"
count=1 

for f in $FILES
do
	folder="$f-untar"
	mkdir "$folder"
	tar "$extract" "$f" -C "$folder"
	mv "$f" "$folder/"
	echo $count
	count=$[count+1]
done

#End of File