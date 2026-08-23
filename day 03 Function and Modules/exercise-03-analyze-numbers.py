# Question 3: Analyze Numbers (Multiple Return Values + Built-ins)

def analyze_numbers(numbers):
    smallest_val = min(numbers)
    largest_val = max(numbers)
    total_val = sum(numbers)
    desc = sorted(numbers, reverse=True)

    return smallest_val, largest_val, total_val, desc

smallest, largest, total, desc = analyze_numbers([4, 9, 1, 7, 3])
print(smallest)
print(largest)
print(total)
print(desc)
