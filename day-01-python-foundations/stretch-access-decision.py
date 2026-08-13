"Stretch Exercise: Dataset Access Decision"

# Given
user_role = "scientist"
is_active = True
requested_dataset = "sales_data"

# Rules
Allowed_roles = ["analyst", "scientist", "engineer"]
Restricted_datasets = ["salary_data", "personal_data"]

# Checking access
if not is_active: 
  access_granted = False
  reason = "Access denied because the user is inactive."
elif user_role not in Allowed_roles:
  access_granted = False
  reason = "Access denied because the role is not allowed."
elif requested_dataset in Restricted_datasets:
  access_granted = False
  reason = "Access denied because the dataset is restricted."
else:
  access_granted = True
  reason = "Access granted successfully."

#Output
if access_granted:
  print(f"Status: Success - {reason}")
else:
  print(f"Status: Fail - {reason}")

# Attempt Scenarios
# Scenario 1 (user_role = "analyst", is_active = True,requested_dataset = "sales_data"): Status: Success - Access granted successfully.Status: Fail - Access granted successfully.
# Scenario 2 (user_role = "Allowed roles", is_active = False, requested_dataset = "sales_data"): Status: Fail - Access denied because the user is inactive.
# Scenario 3 (user_role = "analyst", is_active = True, requested_dataset = "salary_data"): Stuatus:Fail - Access denied because the dataset is restricted.
# Scenario 4 (user_role = "guest"is_active = True, requested_dataset = "sales_data"): Stauts: Status: Fail - Access denied because the role is not allowed.
