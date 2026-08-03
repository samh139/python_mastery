"""
Milestone: m01_collections_mastery
Task: Employee Grouper
"""

raw_employees = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Charlie", "dept": "Engineering"},
    {"name": "David", "dept": "Marketing"},
    {"name": "Eva", "dept": "HR"}
]

# Expected Result:
# {
#     "Engineering": ["Alice", "Charlie"],
#     "HR": ["Bob", "Eva"],
#     "Marketing": ["David"]
# }

## Algorithm
# Loop thru each dict
# find where dept is Engineering
# if dept is engineering, then emp[dept].update(name)

## code-
raw_employees = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Charlie", "dept": "Engineering"},
    {"name": "David", "dept": "Marketing"},
    {"name": "Eva", "dept": "HR"}
]

# Create our empty storage container
result = {}

for emp in raw_employees:
    dept = emp["dept"]
    name = emp["name"]
    
    # Check if this is the first time we see this department
    if dept not in result:
        result[dept] = []  # Initialize an empty list for this new department
        
    # Now it is safe to add the name to the list
    result[dept].append(name)

print(result)
