#!/bin/bash

let a=$(../A/randomNumber.sh 2)
#echo $a
while ! [ $a = 42 ]
do
    echo $a | cat >> howFarFromTruth.txt
    let a=$( ../A/randomNumber.sh 2)
done

echo $a | cat >> howFarFromTruth.txt
