# Summary visualizations of BSCI student survey data
This repository contains summary visualizations of Spring 2024 student survey data from various undergraduate BSCI courses. This README provides a general overview of the data wrangling conducted; for more detailed comments and explanations, as well as the data visualizations themselves, view the Jupyter Notebook.

## Procedure
1. Exported Google Sheet corresponding to Google Form survey as CSV file.
2. Read CSV file into pandas dataframe.
3. Renamed column headers (i.e., questions) to be more succinct.

### Question 1
4. Standardized course codes into
   1. 4 uppercase letters denoting subject (e.g., "BSCI" or "BIOL") followed by
   2. 3 digits and (optionally) a single uppercase letter denoting course number (e.g., "330" or "708W").
5. Resolved discrepancies in responses indicating courses that were not part of those who received the survey (i.e., likely typos) using the course with a minimal Levenshtein distance from the response. **[_currently doing_]**
5. Created bar chart of course distribution amongst respondents.