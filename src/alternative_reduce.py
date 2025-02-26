#!/usr/bin/env python3

import argparse
import os
import json
import matplotlib.pyplot as plt
from glob import glob
from collections import defaultdict

# Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', required=True, help="Directory containing output files")
    parser.add_argument('--hashtags', nargs='+', required=True, help="List of hashtags to analyze")
    return parser.parse_args()

# Function to merge data from .lang or .country files
def merge_data(file_pattern, hashtags):
    hashtag_counts = {hashtag: defaultdict(int) for hashtag in hashtags}

    for filename in sorted(glob(file_pattern)):
        try:
            # Extract the day number from the filename, assuming sequential days (1-365)
            # For simplicity, we'll just count the files (you can adjust this logic if needed)
            day_number = len(hashtag_counts[hashtags[0]]) + 1  # Increment day number sequentially
            print(f"Processing file: {filename}, Day: {day_number}")

            # Open the .lang or .country file
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f"Reading {filename}")

                # Check for each hashtag in the data
                for hashtag in hashtags:
                    if hashtag in data:
                        print(f"Found hashtag #{hashtag} in {filename}")
                        for count in data[hashtag].values():
                            hashtag_counts[hashtag][day_number] += count
                    else:
                        print(f"Hashtag #{hashtag} not found in {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    return hashtag_counts

# Function to plot the data
def plot_data(hashtag_counts, output_file):
    plt.figure(figsize=(10, 5))

    # Plot each hashtag's data (counts per day)
    for hashtag, counts in hashtag_counts.items():
        # Sort days and counts
        days = sorted(counts.keys())
        counts_per_day = [counts[day] for day in days]

        print(f"Plotting hashtag #{hashtag}, Days: {days}, Counts: {counts_per_day}")

        # Plot the data for the hashtag
        plt.plot(days, counts_per_day, label=f"#{hashtag}")

    plt.xlabel("Day Number (1-365)")
    plt.ylabel("Tweet Count")
    plt.title("Hashtag Usage Over Time")
    plt.legend()
    plt.grid()

    # Save the plot to the output file
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()

    print(f"Plot saved as {output_file}")

# Main function
def main():
    args = parse_args()

    # Ensure we look for .lang or .country files in the output directory
    file_pattern = os.path.join(args.output_dir, "geoTwitter20-*.lang*")  # Adjusted pattern to look for .lang files
    hashtag_counts = merge_data(file_pattern, args.hashtags)

    # Check if there is data to plot
    if not any(hashtag_counts.values()):
        print(f"No data to plot for the hashtags {args.hashtags}.")
        return

    # Output file path for the plot
    output_file = os.path.join(args.output_dir, "hashtag_usage_plot.png")
    plot_data(hashtag_counts, output_file)

if __name__ == "__main__":
    main()

