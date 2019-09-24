#! /bin/bash
wget -q -O temp.pdf $1
pdftotext -enc ASCII7 temp.pdf studentData.txt #| sed -e 's/$(echo -ne "\u200b")/@/g' > studentData.txt 
sed -e 's///g' studentData.txt>temp.txt
sed -e '/^$/d' temp.txt>temp2.txt
awk 'BEGIN{FS="\n";RS="-";OFS="\n";ORS="-"} NF<7 {print} ; NF>=7 {for(i=7;i<NF;i++){$6=$6" "$i}; print $1,$2,$3,$4,$5,$6"\n"}' temp2.txt > studentData.txt 
sed -e '/^-$/d' studentData.txt>temp.txt
sed -e '/^$/d' temp.txt > studentData.txt
rm temp.txt
rm temp2.txt
rm temp.pdf
