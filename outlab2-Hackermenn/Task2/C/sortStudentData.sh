#! /bin/bash
awk 'BEGIN{FS="|";OFS="|"} {print $3,$1,$2,$3,$4,$5 | "sort -nr"}' $1>extraField.csv
awk 'BEGIN{FS="|";OFS="|"} {print $2,$3,$4,$5,$6}' extraField.csv > sortedStudentData.csv
sed -e '/Student Name|Roll Number|CPI|Department|Courses Undertaken/d' sortedStudentData.csv>temp.csv
awk 'BEGIN{FS="|";OFS"|";print "Student Name|Roll Number|CPI|Department|Courses Undertaken"} {print}' temp.csv > sortedStudentData.csv
#mv temp.csv sortedStudentData.csv
#echo "sorted"
awk 'BEGIN{FS="|"} (2<=NR)&&(NR<=6) {print $1}' sortedStudentData.csv>top5Students.txt 
rm extraField.csv
rm temp.csv
#LC_ALL=C
#awk 'BEGIN{FS="|";OFS="|"} NR==1 {print } ; NR!=1 {print $1,$2,$3,$4,$5 | "sort -k 3"}' $1>sortedStudentData.csv
#awk 'BEGIN{FS="|";OFS="|"} 2<=NR<=6 {print $1}' sortedStudentData.csv
