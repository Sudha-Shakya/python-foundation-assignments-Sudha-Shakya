"Exercise 5"

# Given
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

# Caculation of failure rate
total_rows = rows_loaded + rows_failed
failure_rate = (rows_failed / total_rows) * 100

# Classification of status
if failure_rate <= 2 and runtime_minutes <= 20:
  status = "Healthy"
elif failure_rate <= 5:
  status = "Warning"
else:
  status = "Critical"

# Output
print(f"Failure rate: {failure_rate:.2f}%")
print(f"Pipeline status: {status}")

# tested with given:
# rows_loaded = 9500, rows_failed = 500, runtime_minutes = 15)
# Output:(Failure rate: 5.24%, Pipeline status: Critical)

# tested with give:
# rows_loaded = 9900, rows_failed = 100,runtime_minutes = 30)
# Output:(Failure rate: 1.00%, Pipeline status: Warning)
# In a final case, since failure rate is low, but runtime is high. It cannot be classified as healthy because we have an 'and' condition requiring the runtime to be <= 20 minutes.
