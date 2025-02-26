import os
import sys
import json
from glob import glob

def merge_files(file_pattern, output_filename):
    """Merge all files matching the pattern into a single output file."""
    merged_data = {}

    for filename in sorted(glob(file_pattern)):
        with open(filename, 'r', encoding='utf-8') as infile:
            try:
                data = json.load(infile)
                
                # Merge data into the merged_data dictionary
                for key, value in data.items():
                    if key not in merged_data:
                        merged_data[key] = {}
                    for subkey, count in value.items():
                        if subkey not in merged_data[key]:
                            merged_data[key][subkey] = 0
                        merged_data[key][subkey] += count

            except json.JSONDecodeError as e:
                print(f"Error reading {filename}: {e}")

    # Write the merged data to the output file
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        json.dump(merged_data, outfile, ensure_ascii=False, indent=4)
    print(f"Data successfully merged into {output_filename}")


if __name__ == "__main__":
    # Ensure an output directory is provided
    if len(sys.argv) != 2:
        print("Usage: python3 reduce.py <output_directory>")
        sys.exit(1)

    output_dir = sys.argv[1]

    # Merge .lang files into all_languages.json
    merge_files(os.path.join(output_dir, "*.lang"), os.path.join(output_dir, "all_languages.json"))

    # Merge .country files into all_countries.json
    merge_files(os.path.join(output_dir, "*.country"), os.path.join(output_dir, "all_countries.json"))

    print("Reduction completed: all_languages.json and all_countries.json have been created.")

