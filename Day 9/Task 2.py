import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
missing_values = grades.isnull()
filled_grades = grades.fillna(0)
filtered_grades = filled_grades[filled_grades > 60]
print("Original Series:\n")
print(grades)
print("\nMissing Values (True means missing):\n")
print(missing_values)
print("\nFilled Series:\n")
print(filled_grades)
print("\nScores Greater Than 60:\n")
print(filtered_grades)