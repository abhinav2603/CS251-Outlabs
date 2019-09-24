#! /bin/bash
wget -q -O temp.pdf $1
pdftotext temp.pdf - | grep -ohi $2 | wc -l
rm temp.pdf

