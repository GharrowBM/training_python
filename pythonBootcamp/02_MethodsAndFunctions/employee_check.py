def employee_check(work_hours: list[tuple[str, int]]):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return employee_of_month, current_max

work_hours = [('Abby', 100), ('Cassie', 1000), ('Billy', 400), ('Emma', 800)]
employee, hours = employee_check(work_hours)

print(f"The employee {employee} is the employee of the month with {hours} hours of work !")