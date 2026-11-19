import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("student.csv")

# Basic information
print("Dataset shape:")
print(data.shape)

print("\nFirst five rows:")
print(data.head())

# Score statistics
average_score = data["score"].mean()
median_score = data["score"].median()
highest_score = data["score"].max()
lowest_score = data["score"].min()

print("\nScore Statistics")
print(f"Average: {average_score:.2f}")
print(f"Median: {median_score:.2f}")
print(f"Highest: {highest_score}")
print(f"Lowest: {lowest_score}")

# Students with scores of 90 or higher
high_scores = data[data["score"] >= 90]

print("\nStudents with scores of 90 or higher:")
print(high_scores[["name", "score"]])

# Average score by grade
average_by_grade = (
    data.groupby("grade")["score"]
    .mean()
    .round(2)
)

print("\nAverage Score by Grade:")
print(average_by_grade)

# Study hours and score correlation
correlation = data["study_hours"].corr(data["score"])

print(f"\nStudy Hours vs. Score Correlation: {correlation:.2f}")

# Scatter plot
plt.scatter(data["study_hours"], data["score"])

plt.xlabel("Study Hours")
plt.ylabel("Test Score")
plt.title("Study Hours vs. Test Scores")

plt.show()