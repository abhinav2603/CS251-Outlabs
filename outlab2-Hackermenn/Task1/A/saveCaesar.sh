#!/bin/bash
read message
var=$(echo "$message" | tr '[a-z][A-Z]' '[a-z][A-Z]')
echo "A" "$var"
for i in {1..25}
do
	a=$(echo $(expr 64 + $i) | awk '{printf("%c",$1)}')
	b=$(echo $(expr 65 + $i) | awk '{printf("%c",$1)}')
#	c=$(echo $(expr 96 + $i) | awk '{printf("%c",$1)}')
#	d=$(echo $(expr 97 + $i) | awk '{printf("%c",$1)}')

	var=$(echo "$message" | tr "$b-ZA-$a" "A-Z" )
	echo $b "$var"
done
read e
read f
echo $e | cat > ./decodedCipher.txt
echo $f | cat >> ./decodedCipher.txt
