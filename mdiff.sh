#!/bin/bash

# $1 & $2 are the versions of firefox to diff
OF=${1}_${2}
echo ${OF}

IN1=../firefox-${1}/*/
IN2=../firefox-${2}/*/

echo ${IN1}

DIFF="/usr/bin/diff -NrBbw "
${DIFF} $IN1 $IN2 | diffstat -f4 > ${OF}
