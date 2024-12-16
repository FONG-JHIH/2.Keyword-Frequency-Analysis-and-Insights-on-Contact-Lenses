# 2.Keyword Frequency Analysis and Insights on Contact Lenses
# Project Overview
This project focuses on the analysis of textual data from comments, with a specific emphasis on content related to "contact lenses" or "hidden eye." Through data cleaning, Chinese word segmentation, and keyword extraction techniques, the program identifies commonly used terms and key content in the data. The results aim to provide valuable insights into user discussions and highlight critical topics.
# Key Features
1.	Data Cleaning and Filtering
o	Filters text containing "contact lenses" or "hidden eye" in titles, content, or comments to focus on relevant subject matter.
o	Removes irrelevant characters (e.g., symbols, URLs) to ensure cleaner and more meaningful text.
2.	Chinese Word Segmentation and Stopword Removal
o	Utilizes the Jieba library for efficient Chinese word segmentation.
o	Customizes a stopword list to exclude meaningless words (e.g., "的," "了," "在").
o	Enhances the accuracy of downstream analyses by reducing noise.
3.	TF-IDF Keyword Extraction
o	Applies TF-IDF algorithm to extract the top 100 significant keywords ranked by their weight scores.
o	Provides insights into the central themes and essential keywords.
4.	Word Frequency Statistics and Report Generation
o	Counts word occurrences and generates a CSV report detailing keywords and their frequencies.
o	Enables further analysis and visualization of the extracted data.
# Program Functionality and Technical Implementation
1.	Data Processing
o	Loads and applies a stopword list to remove irrelevant terms.
o	Combines filtered text for keyword extraction and word frequency analysis.
2.	Text Analysis Techniques
o	Jieba: Used for Chinese word segmentation and TF-IDF keyword extraction.
o	Regular Expressions (re): Utilized for character cleaning and data preprocessing.
o	Pandas: Performs data handling and statistical computations.
3.	Output Results
o	keyword frequency analysis.csv: Saves frequency statistics, including keywords and their occurrence counts.
o	Terminal displays the top keywords, revealing high-frequency terms related to contact lenses.
# Project Structure
•	chinese.txt: Stopword file to exclude meaningless words from the analysis.
•	ptt_data.csv: Input data containing titles, content, and comments.
•	Program code:
o	Data filtering and cleaning.
o	Chinese word segmentation and stopword removal.
o	TF-IDF keyword extraction and word frequency computation.
o	Exporting results to 關鍵詞詞頻分析.csvt.
# Application Scenarios
1.	Industry Analysis: Quickly identify hot topics and user concerns about contact lenses for product improvement or market strategies.
2.	User Insight Discovery: Extract frequent user feedback to help businesses understand user pain points and demands.
3.	Foundation for Text Analysis: Serves as a foundational tool for Chinese text processing in larger natural language processing projects.
# Output Deliverables
1.	Keyword Weight List: Terminal output of the most important keywords and their TF-IDF weights.
2.	Word Frequency Report (CSV): Saves keyword occurrence counts for further visualization and analysis.
# Future Outlook
1.	Enhanced Visualization: Integrate word clouds or bar charts to visualize keyword weights and frequency distributions.
2.	Topic Modeling: Utilize models like LDA to extract hidden topics from the text.
3.	Multi-Language Support: Expand functionality to support English and other languages for broader applications.
This program focuses on data cleaning and analysis of Chinese text, showcasing practical applications of natural language processing techniques. It serves as an excellent highlight project for inclusion in a professional portfolio.
