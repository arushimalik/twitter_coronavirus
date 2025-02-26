import os
import zipfile
import datetime
import json
from collections import Counter, defaultdict
import argparse

# Argument parser for input and output paths
parser = argparse.ArgumentParser(description="Process Twitter dataset for hashtags")
parser.add_argument('input_path', help='Path to the input zip file')
parser.add_argument('output_folder', help='Folder to save the output files')
args = parser.parse_args()

# List of hashtags to track
hashtags = [
    '#코로나바이러스',  # Korean
    '#コロナウイルス',  # Japanese
    '#冠状病毒',        # Chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
]

# Initialize counters for language and country
counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

# Open the zipfile
with zipfile.ZipFile(args.input_path) as archive:
    print(f"Debug: Total files in zip: {len(archive.namelist())}")  # Debugging print

    for filename in archive.namelist():
        print(datetime.datetime.now(), "Processing file:", filename)

        with archive.open(filename) as f:
            for line_number, line in enumerate(f, 1):  # Add line number for debugging
                try:
                    # Parse tweet as JSON
                    tweet = json.loads(line)

                    # Check for tweet data structure
                    tweet_data = tweet.get('data', tweet)  # Fall back to tweet itself if no 'data'

                    # Extract tweet text
                    text = tweet_data.get('text', '')
                    if text:
                        text = text.lower()  # Convert text to lowercase for easier matching
                    else:
                        text = ""

                    # Debug: Print the first few tweet texts to ensure we're reading correctly
                    if line_number <= 5:
                        print(f"Debug: Tweet Text: {text}")  # Print first 5 tweet texts

                    # Extract language (with better check)
                    lang = tweet_data.get('lang', 'unknown')

                    #import code
                    #code.interact(local=locals())

                    # Extract country (check if 'place' and 'country_code' are available)
                    country_code = None
                    try:
                        country_code = tweet['place']['country_code']
                    except (KeyError, TypeError):
                       pass
                    
                    # Debug: Check if country and lang are being extracted correctly
                    if line_number <= 5:
                        print(f"Debug: Lang: {lang}, Country: {country_code}")  # Print first 5 tweets' lang and country

                    # Check if hashtags are present in the tweet
                    for hashtag in hashtags:
                        if hashtag.lower() in text:
                            counter_lang[hashtag][lang] += 1
                            counter_country[hashtag][country_code] += 1

                    # Count overall language and country for all tweets
                    counter_lang["_all"][lang] += 1
                    counter_country["_all"][country_code] += 1

                except json.JSONDecodeError:
                    pass  # Skipping invalid JSON line

# Check if counters have data before saving
if counter_lang and counter_country:
    # Create output folder if it does not exist
    os.makedirs(args.output_folder, exist_ok=True)
    output_path_base = os.path.join(args.output_folder, os.path.basename(args.input_path))

    # Save language dictionary
    output_path_lang = output_path_base + '.lang'
    with open(output_path_lang, 'w') as f:
        json.dump(counter_lang, f, indent=4)

    # Save country dictionary
    output_path_country = output_path_base + '.country'
    with open(output_path_country, 'w') as f:
        json.dump(counter_country, f, indent=4)

else:
    print("No hashtags or country data found in the tweets.")

