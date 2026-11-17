import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("")

# Grouping becomes particulary useful when your dataset
# contains catergories.

# Average score by Grade
average_by_grade = data.groupby("grade")["score"].mean()

print(average_by_grade)