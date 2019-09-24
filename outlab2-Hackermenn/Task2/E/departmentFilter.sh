#! /bin/bash
for records in $1*.txt
	do
	#echo "$records"
	DeptName=$(awk 'BEGIN{RS="-";FS="\n"} {print $4}' $records|sed -e 's/Department://g'| sed -e 's/[[:space:]]//g')
	if [ -d "$DeptName" ] ; then
		cp $records $DeptName
		else
		mkdir $DeptName
		cp $records $DeptName
	fi
	#echo "$DeptName"
	#echo "$records"
	#echo "$deptName"
done
