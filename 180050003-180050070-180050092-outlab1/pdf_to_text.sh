#!/bin/bash

for value in $1/*.pdf
do
    a=$(basename -s .pdf $value)
    cp $value $1"$a.txt"
done

