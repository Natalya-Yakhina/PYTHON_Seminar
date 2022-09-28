def run_work():
    employees = read_csv()
    employee = {}
    while True:
        choice = show_menu()
        if choice == 1: # find employee
            employee = find_employee(employees)
            if employee is None:
                no_employee_error()
            else:
                show_employee_info(employee)

# csv
def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())
# ЗП
def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
            return result