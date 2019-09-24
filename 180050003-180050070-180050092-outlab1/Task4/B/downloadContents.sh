#! /bin/bash
wget -kq -np  -P $2 -r $1
tree -J -o urlReport.json $2
var=($(md5sum urlReport.json))
echo $var
no=$(grep { urlReport.json | wc -l)
echo $no
proname=$(ps -p $no -o command=)
if test -z "$proname"
then 
	echo "No such process"
else 
	echo $proname
fi
