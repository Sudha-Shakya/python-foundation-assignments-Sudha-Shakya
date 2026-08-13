"Exercise 5: Dataset Comparison"

# Given
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}
dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# All unique dataset names
all_unique = dataset_a.union(dataset_b)

# Datasets found in both groups
both_dataset = dataset_a.intersection(dataset_b)

# Datasets only in dataset_a
only_in_dataset_a = dataset_a.difference(dataset_b)

# Datasets only in dataset_b
only_in_dataset_b = dataset_b.difference(dataset_a)

# Output
print(f"All Data Unique: {all_unique}")
print(f"Data Found in Both: {both_dataset}")
print(f"Data only in dataset a: {only_in_dataset_a}")
print(f"Data only in dataset b: {only_in_dataset_b}")
