basic_salary = float(input("Enter your Basic Salary: "))
overtime_hours = float(input("Enter the extra hours you worked: "))
overtime_rate = float(input("Enter your overtime rate: "))
bonus = float(input("Enter your Bonus: "))
tax_percentage = float(input("What is your tax percentage: "))
tax_amount = float(basic_salary*(tax_percentage/100))
gross_salary = basic_salary+(overtime_hours*overtime_rate)-tax_amount
print(gross_salary)
