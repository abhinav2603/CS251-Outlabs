#! /bin/bash
awk ' BEGIN {
	FS=","
	OFS=","
	RS="\r\n"
	ORS="\r\n"
}
{
	t = $1
	$1 = $7
	$7 = t
	print
} ' $1 > new.csv
cp $2 modifiable.csv
sed -i -e '1d' modifiable.csv
#exit
while [ -s modifiable.csv ]
do
	val=$(head -n1 modifiable.csv | grep -oh "[0-9]\{1,\}")
	letGrade=$(head -n1 modifiable.csv | grep -oh "[A-Z][A-Z]")
	sed -i -e "s/^$letGrade/$val/p" new.csv
	sed -i -e '1d' modifiable.csv
done
awk -v sem="$3" -v yr="$4" ' BEGIN {
	FS=","
	x=0
	y=0
	z=0
	RS="\r\n"
}
{
	if(NR>1 && $2==sem && $7==yr)
	{		
		x+=$1*$5
		y+=$5
	}
	z=x/y
}
END { printf("%0.4f\n",z)}' new.csv
rm new.csv
rm modifiable.csv
