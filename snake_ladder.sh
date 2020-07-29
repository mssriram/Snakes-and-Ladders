#!/bin/bash

# program to run snake & ladders game

nlines=`wc -l slinp.dat | awk -F" " '{print $1}'`
cp slinp.dat temp.dat

n1=1
while test $n1 -le $nlines
do
read s1 s2 l1 l2< temp.dat
echo $n1 $s1 $s2 $l1 $l2 
python3 ./snake_ladder.py3 <<%
$s1
$s2
$l1
$l2
%
 
#cp newdata.txt ${s2}_${l2}.dat

nlines1=`expr $nlines - $n1 `
tail -n $nlines1 temp.dat > temp1.dat
mv temp1.dat temp.dat       

n1=`expr $n1 + 1 `
done
