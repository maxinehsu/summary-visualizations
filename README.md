# Summary visualizations of BSCI student survey data
This repository contains summary visualizations, created using Python, of Spring 2024 student survey data from various undergraduate BSCI courses. This README provides a general overview of the data wrangling conducted; for more detailed comments and explanations, as well as the data visualizations themselves, view the Jupyter Notebook.

## Procedure
1. Exported Google Sheet corresponding to Google Form survey as CSV file.
2. Read CSV file into pandas dataframe.
3. Renamed column headers (i.e., questions) to be more succinct.

### Question 1
4. Standardized course codes into
   1. 4 uppercase letters denoting subject (e.g., "BSCI" or "BIOL") followed by
   2. 3 digits and (optionally) a single uppercase letter denoting course number (e.g., "330" or "708W").
5. Resolved discrepancies in responses indicating courses that were not part of those that received the survey (i.e., likely typos) using the course with a minimal Levenshtein distance from the response. **[_currently doing_]**
   - **[6/20/24]** Reconsidering whether modifying based on Levenshtein distance is the best solution. Some responses are tranposed to the wrong course (e.g., BSCI708W does not become BIOL708W). Too many courses have the same minimum Levenshtein distance from the response.
     - A possible solution would be comparing responses to courses lexicographically, or comparing responses to equivalent minimum Levenshtein distance courses lexicographically.
6. Created bar chart of course distribution amongst respondents.
   - **[6/20/24]** Perhaps put courses cross-listed with each other in the same category?
   - **[Ditto]** (_Adena's suggestion_) Perhaps group courses based on category (e.g., BSCI330 and BSCI170/171 would go into the "cell bio" category)?