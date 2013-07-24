#!/bin/bash

base="/Volumes/MilkMaid/release_notes/"
DIRS="/Volumes/MilkMaid/release_notes/*"
count=1

for d in $DIRS
do
	for f in "$d/releasenotes/*"
	do
		echo $f
		targetfilename="$(basename $d)"
		extension=".html"
		if [ "$f" == "buglist.html" ]
		then
			targetfilename="$(basename $d)-buglist"
		fi	
		echo $targetfilename
		
		echo "$base$targetfilename"
		#mv "$f" "$base$targetfilename"
		echo $count
		count=$[count+1]
	done
	#rm -r $d/releasenotes
done

#End of File