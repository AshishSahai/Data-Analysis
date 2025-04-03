employee_performance = {
    "John": {"Project A": 85, "Project B": 78, "Project C": 92},
    "Emma": {"Project A": 90, "Project B": 88, "Project C": 95},
    "Mike": {"Project A": 75, "Project B": 80, "Project C": 85}
}
employee_data = {}
employee_average = {}
for name, projects in employee_performance.items():
    total_each_employee = sum(projects.values())
    employee_data[name] = total_each_employee
    n = len(projects)
    employee_average[name] = total_each_employee/n
    print(employee_average)

    print(f"Average total of {name} : {total_each_employee/n}")

top_performer = max(employee_data, key=employee_data.get)

print(f"Top performing employee: {top_performer}")
