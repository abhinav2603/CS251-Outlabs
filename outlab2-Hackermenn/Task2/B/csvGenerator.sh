#! /bin/bash
sed -e 's/-\{1,\}/-/g' $1| sed -e 's/[a-zA-Z[:space:]]\{1,\}://g' | sed -e '/^$/d'| awk 'BEGIN{OFS="|";RS="-";FS="\n"; print "Student Name|Roll Number|CPI|Department|Courses Undertaken"} NR!=1 {print $2,$3,$4,$5,$6}' > studentData.csv
#sed -e 's/^[a-zA-Z[:space:]]\{1,\}://g' $1 | sed -e 's/-\{1,\}/-/g' |sed -e 's/$(echo -ne '\u200b')/:/g' > fieldNameRemoved.txt 
#awk 'BEGIN{OFS='|';FS='\n';RS='\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-'} fieldNameRemoved.txt
