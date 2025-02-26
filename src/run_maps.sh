#!/bin/bash

# Define input directory and output directory
INPUT_DIR="/data/Twitter dataset"
OUTPUT_DIR="./output"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop over all tweet files from 2020 (geoTwitter20-*)
for file in "$INPUT_DIR"/geoTwitter20-*.zip; do
    # Extract just the filename (for logging purposes)
    filename=$(basename "$file")

    # Run map.py on each file in parallel using nohup
    echo "Processing $filename..."
    nohup python3 map.py "$file" "$OUTPUT_DIR" > "logs/$filename.log" 2>&1 &

done

echo "All map.py processes have been started in parallel."

