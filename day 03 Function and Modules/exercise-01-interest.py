#Question 1: Simple Interest Calculator (Default Arguments)

def calculate_simple_interest(principal, rate=5, time=1):

  interest= (principal * rate* time)/100
  return interest

print(calculate_simple_interest(1000, 10, 2))   # -> 200.0
print(calculate_simple_interest(1000))          # -> 50.0   (uses default rate=5, time=1)
print(calculate_simple_interest(2000, time=3))  # -> 300.0  (uses default rate=5)
