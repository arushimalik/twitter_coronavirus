#!/usr/bin/env python3

# Command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
args = parser.parse_args()

# Imports
import os
import json
import matplotlib.pyplot as plt

# Open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# Normalize the counts by the total values if --percent flag is used
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# Sort the count values from low to high and get the top 10
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)
top_items = items[:10]
keys, values = zip(*top_items)

# Extract filename from input_path (e.g., "all_languages" or "all_countries")
input_filename = os.path.basename(args.input_path).replace(".json", "")

# Create the bar graph
plt.figure(figsize=(10, 5))
plt.barh(keys, values, color='skyblue')
plt.xlabel("Count")
plt.ylabel("Language/Country")
plt.title(f"Top 10 for {args.key} in {input_filename}")
plt.gca().invert_yaxis()

# Save the bar graph with a unique filename
output_filename = f"{input_filename}_{args.key.replace('#', '')}_top_10_bargraph.png"
plt.savefig(output_filename, bbox_inches="tight")
plt.close()

print(f"Bar graph saved as {output_filename}")

