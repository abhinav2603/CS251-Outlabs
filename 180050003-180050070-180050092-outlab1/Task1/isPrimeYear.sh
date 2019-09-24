#!/bin/bash

re='^[0-9]+$'
if ! [[ $1 =~ ^[0-9]+$ ]]
then
	echo "Invalid argument!" >&2
else
	if [ $1 -ge 2 ]
	then
		let count=0
		let i=2
		let j=4
		while [ $j -le $1 ]
		do
			let temp=$1%$i
			if [[ $temp == 0 ]]
			then
				let count++
				break
			fi
			let i++
			let j=$i*$i
		done
		if [[ $count == 0 ]]
		then
			echo "Prime Year!"
		else
			echo "Not a prime year."
		fi
	elif [[ $1 == 1 ]]
	then
		echo "Not a prime year."
	else
		echo "Invalid argument!"
	fi
fi
