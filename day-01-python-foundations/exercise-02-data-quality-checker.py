"Exercise 2"

# Data Quality Checker
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# Caculation
problematic_rows = missing_rows + duplicate_rows
problem_percentage = (problematic_rows / total_rows) * 100

# Classify of data set rules
if problem_percentage <= 0.02:
  Classification = "Excellent"
elif problem_percentage <= 0.05:
  Classification = "Acceptable"
else:
 Classification = "Needs Cleaning"

# Output
print(f"Total_rows: {total_rows}")
print(f"Problematic_rows: {problematic_rows}")
print(f"Problem_percentage: {problem_percentage:.2f}%")
print(f"Final_classification: {Classification}")
