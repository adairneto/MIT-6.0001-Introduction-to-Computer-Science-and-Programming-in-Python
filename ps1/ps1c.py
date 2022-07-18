# User inputs
annual_salary = float(input("Enter your annual salary: "))

# Constants
r = 0.04
portion_down_payment = 0.25
semi_annual_raise = 0.07
total_cost = 1000000
down_payment = portion_down_payment * total_cost

# Bisection search variables
epsilon = 100 
min_savings_rate = 0
max_savings_rate = 10000
steps = 0

# How much I still need
dp_savings_diff = down_payment

# Returns difference between down_payment and savings
def calculate_dp_savings_diff(savings_rate,annual_salary):
    """
    Parameters
    ----------
    savings_rate : int
        savings rate of salary.
    annual_salary : int
        salary in which rate applies.

    Returns
    -------
    Difference between down_payment and savings (int).
    """
    # Start variables
    current_savings = 0
    months = 0

    # Accumulates the money in the period of 36 months
    for months in range(36):
        return_investment = current_savings * r / 12
        portion_monthly_salary = savings_rate * annual_salary/120000
        current_savings += return_investment + portion_monthly_salary
        months += 1
        
        # Raise every six months   
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    
    return down_payment - current_savings

# Evaluates if even with the higher savings rate it won't be possible to save enough
if calculate_dp_savings_diff(max_savings_rate,annual_salary) > 0:
    print("It is not possible to pay the down payment in three years")
    exit()
    
# Stops when the current savings are within the epsilon (bisection search)
while dp_savings_diff > epsilon and max_savings_rate - min_savings_rate > 1:
    mp_savings_rate = (min_savings_rate + max_savings_rate) // 2
    min_diff = calculate_dp_savings_diff(min_savings_rate, annual_salary)
    mp_diff = calculate_dp_savings_diff(mp_savings_rate, annual_salary)

    # Intermediate Value Theorem
    if (min_diff > 0) == (mp_diff > 0):
        min_savings_rate = mp_savings_rate
    else:
        max_savings_rate = mp_savings_rate

    steps += 1
    dp_savings_diff = abs(mp_diff)

print('Best savings rate: {:0.4f}'.format(mp_savings_rate / 10000))
print('Steps in the bisection search: %d' % steps)