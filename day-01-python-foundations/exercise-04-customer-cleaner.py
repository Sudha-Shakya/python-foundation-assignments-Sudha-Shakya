"Exercise 4"

# Given
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Cleaning the given value
name = raw_name.strip().title()
city = raw_city.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

# Use a ternary expression for the adult status
status = "Adult" if age >=18 else "Minor"

# Display Output
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")
