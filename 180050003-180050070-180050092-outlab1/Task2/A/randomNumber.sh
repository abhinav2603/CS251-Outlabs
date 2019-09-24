#!/bin/bash

single_digit(){
    c=$1
    d=$(expr $c % 9)
    d=$(expr $d + 1)
    #echo $c $d
}
single(){
    d=$(expr $1 % 10)
}


b=$(od -A n -t d -N 1 /dev/urandom)
#echo $b
single_digit $b
a=$d
#echo $a
f=1

while [ $f -lt $1 ]
do
    b=$(od -A n -t d -N 1 /dev/urandom)
    single $b
    e=$d
    a=$(( a * 10))
    let a=$(( a + e ))
    let f++
done
echo $a


