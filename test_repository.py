
from src.database.repository import (
    add_elective,
    get_all_electives,
    delete_elective
)

# Insert a demo elective
new_id = add_elective(
    course_code="DEMO-001",
    course_name="Introduction to Artificial Intelligence",
    credit_hours=3.0,
    prerequisites=["Programming Fundamentals"],
    semester=6
)

print("Elective inserted successfully!")
print("New elective ID:", new_id)


# Retrieve all electives
electives = get_all_electives()

print("\nAll Electives:")

for elective in electives:
    print(elective)


# Delete our demo record
delete_elective(new_id)

print("\nDemo elective deleted successfully!")