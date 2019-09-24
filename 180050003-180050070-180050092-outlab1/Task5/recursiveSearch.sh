#!/bin/bash

if [ $# -eq 0 ]
then
    a="Usage:./recursiveSearch.sh <words-to-search>"
    echo $a
    exit 1
else
    
    result=$(grep -rnv '^$' Data) #grep -rn --include=\*.txt "" ./)
    #result=$(echo "$result" | sort)
    #echo $result
	for i in $@
	do
	    if [ -z result ]
	    then
			break
    	fi   
		result=$(echo "$result" | grep -hiw $i)
	done

	echo "$result"
fi

     
