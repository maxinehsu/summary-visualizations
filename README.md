# Summary visualizations of BSCI student survey data
Summary visualizations of Spring 2024 student survey data from various undergraduate BSCI courses.

> [!IMPORTANT]
> **UPDATE 6/13/24:** I have decided to transfer my Python code to a Jupyter Notebook. This enables display of graphs and other data visualizations that may be present throughout my code. I can also embed Markdown between code blocks, facilitating code readability.

## Procedure
1. Exported Google Sheet corresponding to Google Form survey as CSV file for easier Python data wrangling.
2. Read CSV file into pandas dataframe.
3. Renamed column headers (i.e., questions) to be more succinct.

### Question 1
4. Standardized course codes into
   1. 4 uppercase letters denoting subject (e.g., "BSCI" or "BIOL") followed by
   2. 3 digits and (optionally) a single uppercase letter denoting course number (e.g., "330" or "708W").
5. Created histogram of course distribution amongst respondents. **[_currently doing_]**