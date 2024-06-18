# Summary visualizations of BSCI student survey data
Summary visualizations of Spring 2024 student survey data from various undergraduate BSCI courses.

## Procedure
1. Exported Google Sheet corresponding to Google Form survey as CSV file for easier Python data wrangling.
2. Read CSV file into pandas dataframe.
3. Renamed column headers (i.e., questions) to be more succinct.

### Question 1
4. Standardized course codes into **[_currently modifying_]**
   1. 4 uppercase letters denoting subject (e.g., "BSCI" or "BIOL") followed by
   2. 3 digits and (optionally) a single uppercase letter denoting course number (e.g., "330" or "708W").
5. Created bar chart of course distribution amongst respondents.