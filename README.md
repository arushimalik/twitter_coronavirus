Coronavirus Twitter Analysis

This project analyzes the spread of the coronavirus on the social media platform Twitter. It processes huge datasets of tweets using the MapReduce procedure and gathers information and data on how tweets with different hashtags to see how they have spread all over the world. It then visualizes the results using different techniques, providing us with an insightful view of hashtag usage by language, country, and over time.

Main files created include: 
- Map: Created a map.py file to count tweets using different hashtags by various languages and countries.
- Reduce: Made a reduce.py file which aggregates the tweet counts and then gathers all the data together into two different files.
- Visualization: Updated the visualize.py file to create bar charts for the top 10 languages and countries using specific hashtags. I created four bar charts for the hashtags #coronavirus and #코로나바이러스, two for languages and two for countries. Here I have attached my bar plots:
    - <img width="650" alt="Top 10 for #coronavirus in all_countries" src="https://github.com/user-attachments/assets/50540d89-f62b-44cf-be1e-4178bbd7e6e3" />
    - <img width="650" alt="Top 10 for #코로나바이러스 in all_languages" src="https://github.com/user-attachments/assets/c6c4b84c-1744-46a2-9265-b795b13558fd" />
<img width="650" alt="Top 10 for #코로나바이러스 in all_countries" src="https://github.com/user-attachments/assets/a4f702e4-a376-49fb-9b97-9c838f2459c8" />
<img width="650" alt="Top 10 for #coronavirus in all_languages" src="https://github.com/user-attachments/assets/c1c4a46c-75b7-4cac-94c3-432da650975b" />
- Alternative Reduce: Made an alternative_reduce.py that makes a plot with a line per input hashtag and x-axis is the day of the year and the y-axis is the number of tweets that use that hashtag during the year. Here is my line plot:
  - <img width="650" alt="Line Plot for #coronavirus and #코로나바이러스" src="https://github.com/user-attachments/assets/567cbb5e-b21b-4442-ad7a-9efd763e6361" />


