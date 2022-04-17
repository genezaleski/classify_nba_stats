#!/usr/bin/sh

file=$1
filteredFile=$file"_filtered"

#Get correctly formatted columns
awk '{print $1 " " $2 "," $4 " " $5}' $file > $filteredFile
# replace newlines with commas
sed -zi 's/\n/,/g;s/,$/\n/' $filteredFile
# replace duplicate commas
sed -i "s+,\s++g" $filteredFile 
# new line on years starting with 2
sed -i "s+,2+\n2+g" $filteredFile 
# new line on years starting with 1
sed -i "s+,1+\n1+g" $filteredFile 

# destroy the evidence
rm $file
mv $filteredFile $file
