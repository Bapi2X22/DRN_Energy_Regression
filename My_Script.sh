#!/bin/bash

cd /eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/test

# Input file list
input_list="input_files.txt"

# Check if input list exists
if [[ ! -f $input_list ]]; then
    echo "Error: $input_list not found!"
    exit 1
fi

# Initialize the iteration counter
count=1

cmsenv

# Loop through input files
while IFS= read -r input_file; do
    # Skip empty lines and comments
    [[ -z "$input_file" || "$input_file" == \#* ]] && continue

    # Generate output file with an iteration number (e.g., miniAOD_001.root)
    output_file=$(printf "miniAOD_%03d.root" $count)

    echo "Processing input: $input_file"
    echo "Output will be: $output_file"

    echo "Running cmsRun with inputFile=$input_file and outputFile=$output_file"

    # Run cmsRun with dynamic input and output filenames
    cmsRun Zee_dumper_MINIAOD_MC_cfg_copy.py inputFile="$input_file" outputFile="$output_file"

    # Increment the counter
    ((count++))

done < "$input_list"

echo "All jobs completed!"
