"Exercise 3"

# File Validator
file_name = "file_name.strip().lower()"

# Validation for file extension
if file_name.endswith == (".csv"):
  Status = "Valid CSV file"
elif file_name.endswith == (".json"):
  Status = "Valid JSON file"
elif file_name.endswith == ("parquet"):
  Status = "Valid PARQUET file"
else:
  Status = "Invalid file! Only .csv, .jason, .parquet are allowed"

# Output
print (f"file status: {Status}")
