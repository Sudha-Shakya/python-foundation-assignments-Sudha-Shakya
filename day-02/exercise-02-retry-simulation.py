"Exercise 2: Retry Simulation"

# Given variables
attempt = 1
max_attempts = 3
operation_successful = False

# Using while loop
while attempt <= max_attempts:
  print(f"Attempt {attempt}")

# Using break if the operation succeeds in second attmept
  if attempt == 2:
    operation_successful = True
    break
  attempt = attempt + 1

# Output
if operation_successful:
    print("Operation completed sucessfully")
else:
    print("Operation failed after three attempt")
