# List of employees
employees = [
    {
        "ID": 1,
        "Name": "John Doe",
        "Department": "Sales",
        "Age": 30,
        "Email": "john.doe@company.com"
    },
    {
        "ID": 2,
        "Name": "Jane Smith",
        "Department": "Human Resources",
        "Age": 25,
        "Email": "jane.smith@company.com"
    },
    {
        "ID": 3,
        "Name": "Mark Johnson",
        "Department": "IT",
        "Age": 40,
        "Email": "mark.johnson@company.com"
    },
    {
        "ID": 4,
        "Name": "Lisa Wong",
        "Department": "Marketing",
        "Age": 28,
        "Email": "lisa.wong@company.com"
    },
    {
        "ID": 5,
        "Name": "Paul McDonald",
        "Department": "Finance",
        "Age": 35,
        "Email": "paul.mcdonald@company.com"
    }
]

# Loop through the list of employees and print their details
for employee in employees:
    print(f"ID: {employee.get('ID')}, Name: {employee.get('Name')}, Department: {employee.get('Department')}, Age: {employee.get('Age')}, Email: {employee.get('Email')}")