#!/bin/bash
awk ' NR<=3 {
		for(i=1;i<=NF;i++)
		{
			printf("%20s",$i)
		}
		print ""
	} ' $1
sed -n -e "/$2/ p" $1 | sed -n -e "/$3/ p" | awk '{print $0 | "sort -k 3"}'
