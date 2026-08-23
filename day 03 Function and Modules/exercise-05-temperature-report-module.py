# Question 5:Temperature Report Module (Custom Module + Standard Library)

#Part A

module_code = '''
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

MODULE_VERSION = "1.0"
'''

with open("temperature_utils.py", "w") as f:
    f.write(module_code)

print("temperature_utils.py created. Now fill in the functions above, then re-run this cell.")
