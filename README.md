# Keyword-Frequency-Analysis-of-Data-Scraped-from-the-PTT-Social-Networking-Website
Data scraped from PTT usually contains large amounts of titles, content, and comments, which can be further analyzed to extract valuable information through keyword frequency analysis.
Feature Description:
•	Cleans the scraped data to remove meaningless characters and noise (e.g., punctuation marks, HTML tags).
•	Performs Chinese word segmentation to extract high-frequency keywords (e.g., product names, feature descriptions, consumer demands).
•	Utilizes the TF-IDF (Term Frequency-Inverse Document Frequency) algorithm for weight calculation to filter out impactful keywords.
Technical Highlights:
•	Uses the Python jieba library for Chinese word segmentation and frequency statistics.
•	Develops a custom stop-word list to improve analysis accuracy.
•	Outputs frequency results to a CSV file, including each keyword and its corresponding occurrence count and weight.
Application Scenarios:
•	Product Development: Analyzing consumer focus and demands for specific products.
•	Marketing Strategies: Extracting popular topics to plan targeted marketing strategies.
•	Exploratory Data Analysis: Gaining initial insights into core content and trends of consumer discussions.
