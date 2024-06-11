import pandas as pd
import re

df = pd.read_csv("student_responses.csv")

# rename column headers to be more succinct
df.columns = ["Timestamp",
              "Course",                             # Q1
              "Learned about comp bio how?",        # Q2
              "Courses w/ comp bio",                # Q3
              "Time on comp bio",                   # Q4
              "Instructor support",                 # Q5
              "Course resource support",            # Q6
              "Most helpful",                       # Q7
              "Frustrations",                       # Q8
              "Add. info",                          # Q9
              "Graduating",                         # Q10
              "Job app/acceptance impact",          # Q11
              "Career plan impact",                 # Q12
              "Demographics",                       # Q13
              "Email"]                              # Q14

# each respondent's unique identifier is the corresponding row's index


### QUESTION 1 ###

# regexes to look for
subject_pattern = re.compile("[A-Za-z]{4}")         # e.g., "BSCI" or "BIOE"
number_pattern = re.compile("[0-9]{3}[A-Za-z]?")    # e.g., "171" or "330"

# iterate through each element of the "Course" column
for i in range(len(df["Course"])):
    subject = number = ""
    subject_match = subject_pattern.match(df["Course"][i])
    number_match = number_pattern.match(df["Course"][i])

    if subject_match:
        pass
    if number_match:
        pass