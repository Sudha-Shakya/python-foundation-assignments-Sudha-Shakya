"Exercise 1: Batch Processor"

# Use a for loop and range() to print batch numbers from 1 to 10
for batch_number in range (1, 11):
  print(f"Processing batch {batch_number}")

# Modulo operator
  if batch_number % 3 == 0:
    print("Checkpoint_reached")
