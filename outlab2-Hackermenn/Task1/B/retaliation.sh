#!/bin/bash
read message
i=$(printf "%d" \'"$1")
j=$(expr $i - 1 )
#echo $j
a=$(echo $i | awk '{printf("%c",$1)}')
b=$(echo $j | awk '{printf("%c",$1)}')

if [ $i -eq 65 ]
then
	echo "$message"
else
	var=$(echo "$message" | tr "A-Z" "$a-ZA-$b")
	echo "$var"
fi

