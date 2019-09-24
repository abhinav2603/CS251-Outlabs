#! /bin/bash
sed -e 's/-\{1,\}/-/g' $1| sed -e 's/[a-zA-Z[:space:]]\{1,\}://g' | sed -e '/^$/d'  >temp.txt
awk 'BEGIN{FS="\n";RS="-";OFS="\n"} NR!=1 {print "Student Name:"$2,"Roll Number:"$3,"CPI:"$4,"Department:"$5,"Courses Undertaken:"$6 >$3".txt"}' temp.txt
rm temp.txt
#for file in * 
#do
#	if [[ "$file" =~ "*"]]
#	then
#	 echo "$file matched this"
#	else
#	mv $file $file".txt"
#	fi
#done
