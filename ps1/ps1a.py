# User inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Initial data
current_savings = 0
r = 0.04
portion_monthly_salary = portion_saved * annual_salary / 12 
portion_down_payment = 0.25
months = 0

# Loop
while current_savings < portion_down_payment * total_cost:
    return_investment = current_savings * r / 12
    current_savings += return_investment + portion_monthly_salary
    months += 1

print("\nNumber of months: %d" % months)