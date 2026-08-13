"Exercise 3: Clean Numeric Values"

# Given:
raw_values = [100, None, 250, "invalid", 300, None, 450]
clean_values_loop = []

for val in raw_values:
  if not isinstance(val,int):
    continue
  clean_values_loop.append(val)
  clean_values_comp = [val for val in raw_values if isinstance(val, int)]

# Output
print(f"loop result: {clean_values_loop}")
print(f"Comprehension Result: {clean_values_comp}")
