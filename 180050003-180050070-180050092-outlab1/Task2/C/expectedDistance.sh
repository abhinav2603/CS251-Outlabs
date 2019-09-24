#!/bin/bash

#read k

let a=0
let b=1

while [ $b -le $1 ]
do
	../B/findTheAnswer.sh
    let c=$(wc -l  < howFarFromTruth.txt)
    rm howFarFromTruth.txt
    let a=$(expr $a + $c)
    let b++
done

let b=$(expr $a / $1)
echo $b
