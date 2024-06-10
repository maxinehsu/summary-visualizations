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
              "Job application/acceptance impact",  # Q11
              "Career impact",                      # Q12
              "Demographics",                       # Q13
              "Email"]                              # Q14


### QUESTION 1 ###

# regex to look for
course = re.compile("([A-Za-z]{4})[ -]*([0-9]{3}[A-Za-z]?)")

for i in df.get("Course"):
    pass