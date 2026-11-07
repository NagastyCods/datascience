import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student.csv")
print(data)
# to view the first 5 rows of the dataset
print(data.head())
# to view the dimensions of the dataset
print(data.shape)
# to view the columns of the dataset
print(data.columns)
# to view the data types of the columns
data.info()
# calculating basic statistics
# finding the average of the marks column
average_score = data["score"].mean()
print(f"The average score of the students is: {average_score:.2f}")

# finding the highest and lowest scores
highest_score = data["score"].max()
lowest_score = data["score"].min()
print(f"The highest score is: {highest_score}")
print(f"The lowest score is: {lowest_score}")

# find the median score
median_score = data["score"].median()
print(f"The median score is: {median_score}")
# generating a statistical summary
print(data["score"].describe())