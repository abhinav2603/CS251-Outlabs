#!/bin/bash
a=$(cut -d ',' -f 1,2,3 $1)
b=$(cut -d ',' -f 1,4,5 $1)
c=$(cut -d ',' -f 1,6,7 $1)
echo "$a" >> $2
echo "$b" >> $2
echo "$c" >> $2
sort -k3,3 -f -t ',' -o $2 $2
