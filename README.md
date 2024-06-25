# Summary visualizations of BSCI student survey data
This repository contains summary visualizations, created using Python, of Spring 2024 student survey data from various undergraduate BSCI courses. This README provides a general overview of the data wrangling conducted; for more detailed comments and explanations, as well as the data visualizations themselves, view the Jupyter Notebook file `viz.ipynb`.

The :arrow_left: indicates what I am currently working on.

## Procedure
1. Exported Google Sheet corresponding to Google Form survey as `student_responses.csv`.
2. Read `student_responses.csv` into pandas dataframe.
3. Renamed column headers (i.e., questions) as question numbers.

### Question 1
4. Standardized course codes into
   1. 4 uppercase letters denoting subject (e.g., "BSCI" or "BIOL") followed by
   2. 3 digits and (optionally) a single uppercase letter denoting course number (e.g., "330" or "708W").
5. Resolved discrepancies in responses indicating courses that were not part of those that received the survey (i.e., likely typos) using the course with a minimal [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) from the response. :arrow_left:
   - **6/20/24** | Reconsidering whether modifying based on Levenshtein distance is the best solution. Some responses are tranposed to the wrong course (e.g., BSCI708W does not become BIOL708W). Too many courses have the same minimum Levenshtein distance from the response.
     - A possible solution would be comparing responses to courses lexicographically (based on dictionary order), or comparing responses to equivalent minimum Levenshtein distance courses lexicographically.
6. Created bar chart of course distribution amongst respondents.
   - **6/20/24** | Perhaps put courses cross-listed with each other in the same category?
   - **6/20/24** | (_Adena's suggestion_) Perhaps group courses based on category (e.g., BSCI330 and BSCI170/171 would go into the "cell bio" category)?

### Question 4
7. Created bar chart of time spent completing computational biology coursework amongst respondents. :arrow_left:
   - **6/21/24** | Have to debug. For some reason the x-axis labels are being sorted in ascending order even though I never sorted them as such. As a result, the numerical labels, when shown, are way off (and in the wrong order).

### Question 10
8. Created bar chart of graduation statistics.

### Question 11
9. Created bar chart of job application/acceptance statistics. :arrow_left:
   - **6/24/24** | Realized pandas, by default, interprets "NA" and empty string values from a CSV file as "NaN". This becomes a problem when a question allows both a "NA" response and no response at all (i.e., is an optional question). This is the case for Question 11.