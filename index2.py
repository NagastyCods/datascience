import pandas as pd
import matplotlib.pyplot as plt 

# importing the dataset
data = pd.read_csv("student.csv")
# finding student with high score

high_scores = data[data["score"] >=90]
print(high_scores)
# finding student who score more than 5 hours
# uisng the function idmax()

top_student_index = data["score"].idxmax()
top_student = data.loc[top_student_index]

print(top_student)

# multiple statistics

grade_summary = data.groupby("grade")["score"].agg(["mean", "max", "min", "count"])

print(grade_summary)