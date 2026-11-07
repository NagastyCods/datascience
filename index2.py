import pandas as pd
import matplotlib.pyplot as plt 

# importing the dataset
data = pd.read_csv("student.csv")
# finding student with high score

high_scores = data[data["score"] >=90]
print(high_scores)