import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("student.csv")

plt.scatter(data["study_hours"], data["score"])

plt.xlabel("Study Hours")
plt.ylabel("Test scores")
plt.title("Study Hours vs. Test Scores")

plt.show()

