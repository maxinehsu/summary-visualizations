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
              "Additional info",                    # Q9
              "Graduating",                         # Q10
              "Job app/acceptance impact",          # Q11
              "Career plan impact",                 # Q12
              "Demographics",                       # Q13
              "Email"]                              # Q14


### QUESTION 1 ###

# regex to look for
course = re.compile("([A-Za-z]{4})[ -]*([0-9]{3}[A-Za-z]?)")

# iterate through all elements of the "Course" column
for i in range(len(df["Course"])):
    # ignore first element (question)
    if i == 0:
        continue

    subject = number = ""
    m = course.match(df["Course"][i])

    if m.group(1):
        subject = m.group(1).upper()    # standardize to uppercase
    if m.group(2):
        number = m.group(2).upper()     # standardize to uppercase