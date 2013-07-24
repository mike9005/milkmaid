#!/bin/bash

SUM=0
for i in `cat *.*`
do
	SUM=$(($SUM + $i))
done
echo $SUM

#End of script
