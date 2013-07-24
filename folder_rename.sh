#!/bin/bash

FOLDERS="/Volumes/MilkMaid/raw_source"
for f in $(ls $FOLDERS)
do
	name=${f%%[-.]source*}
	mv "$FOLDERS/$f" $FOLDERS/$name
done

#End of File