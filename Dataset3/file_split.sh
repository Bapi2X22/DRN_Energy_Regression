#!/bin/bash

input_file="file_3.txt"
lines_per_file=500

# Split the file into chunks of 500 lines
count=0
start=1
while [ $start -le $(wc -l < "$input_file") ]; do
    end=$((start + lines_per_file - 1))
    count=$((count + 1))
    
    output_file="part_${count}.txt"
    
    echo "Creating $output_file with lines $start to $end"
    awk "NR>=$start && NR<=$end" "$input_file" > "$output_file"

    start=$((end + 1))
done
